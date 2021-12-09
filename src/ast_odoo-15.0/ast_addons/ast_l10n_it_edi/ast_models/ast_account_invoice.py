Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='date', asname=None),
                alias(name='datetime', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
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
            module='odoo.tools',
            names=[alias(name='float_repr', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_mail_server',
            names=[alias(name='MailDeliveryException', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='Form', asname=None)],
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
        Assign(
            targets=[Name(id='DEFAULT_FACTUR_ITALIAN_DATE_FORMAT', ctx=Store())],
            value=Constant(value='%Y-%m-%d', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='AccountMove',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='account.move', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_send_state', ctx=Store())],
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
                                            Constant(value='new', kind=None),
                                            Constant(value='New', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='other', kind=None),
                                            Constant(value='Other', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='to_send', kind=None),
                                            Constant(value='Not yet send', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sent', kind=None),
                                            Constant(value='Sent, waiting for response', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='invalid', kind=None),
                                            Constant(value='Sent, but invalid', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='delivered', kind=None),
                                            Constant(value='This invoice is delivered', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='delivered_accepted', kind=None),
                                            Constant(value='This invoice is delivered and accepted by destinatory', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='delivered_refused', kind=None),
                                            Constant(value='This invoice is delivered and refused by destinatory', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='delivered_expired', kind=None),
                                            Constant(value='This invoice is delivered and expired (expiry of the maximum term for communication of acceptance/refusal)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='failed_delivery', kind=None),
                                            Constant(value='Delivery impossible, ES certify that it has received the invoice and that the file                         could not be delivered to the addressee', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='to_send', kind=None),
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
                    targets=[Name(id='l10n_it_stamp_duty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Dati Bollo', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='draft', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_ddt_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='l10n_it.ddt', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='DDT', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='draft', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
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
                    targets=[Name(id='l10n_it_einvoice_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_it_einvoice', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_einvoice_id', ctx=Store())],
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
                                value=Constant(value='Electronic invoice', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_l10n_it_einvoice', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_l10n_it_einvoice',
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
                            targets=[Name(id='fattura_pa', ctx=Store())],
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
                                args=[Constant(value='l10n_it_edi.edi_fatturaPA', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='einvoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='edi_document_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='d', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='d', ctx=Load()),
                                                        attr='edi_format_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='fattura_pa', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='l10n_it_einvoice_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='einvoice', ctx=Load()),
                                        attr='attachment_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='l10n_it_einvoice_name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='einvoice', ctx=Load()),
                                            attr='attachment_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
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
                            args=[
                                Constant(value='edi_document_ids', kind=None),
                                Constant(value='edi_document_ids.attachment_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_before_xml_exporting',
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
                            targets=[Name(id='errors', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.edi.format', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_l10n_it_edi_check_invoice_configuration',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='errors', ctx=Load()),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.edi.format', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_format_error_message',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Invalid configuration:', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Name(id='errors', ctx=Load()),
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
                    name='invoice_generate_xml',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='report_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.edi.format', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_l10n_it_edi_generate_electronic_invoice_filename',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=BinOp(
                                left=Constant(value="<?xml version='1.0' encoding='UTF-8'?>", kind=None),
                                op=Add(),
                                right=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_export_as_xml',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='description', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[
                                    Constant(value='Italian invoice: %s', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_type',
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
                                            Constant(value='res_id', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='raw', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Name(id='report_name', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='description', ctx=Load()),
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
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=BinOp(
                                            left=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='E-Invoice is generated on %s by %s', kind=None)],
                                                keywords=[],
                                            ),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='now',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='attachment', kind=None)],
                                values=[Name(id='attachment', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_fatturapa_export_values',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='format_date',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='dt', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dt', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='dt', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dt', ctx=Load()),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='DEFAULT_FACTUR_ITALIAN_DATE_FORMAT', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='format_monetary',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='number', annotation=None, type_comment=None),
                                    arg(arg='currency', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='float_repr', ctx=Load()),
                                        args=[
                                            Name(id='number', ctx=Load()),
                                            Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Constant(value=2, kind=None),
                                                    Attribute(
                                                        value=Name(id='currency', ctx=Load()),
                                                        attr='decimal_places',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
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
                            name='format_numbers',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='number', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='number_splited', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='number', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='number_splited', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value='%.02f', kind=None),
                                                op=Mod(),
                                                right=Name(id='number', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='cents', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='number_splited', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='cents', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=8, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value='%.08f', kind=None),
                                                op=Mod(),
                                                right=Name(id='number', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='float_repr', ctx=Load()),
                                        args=[
                                            Name(id='number', ctx=Load()),
                                            Call(
                                                func=Name(id='max', ctx=Load()),
                                                args=[
                                                    Constant(value=2, kind=None),
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='cents', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                            name='format_numbers_two',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='number', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Constant(value='%.02f', kind=None),
                                        op=Mod(),
                                        right=Name(id='number', ctx=Load()),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='discount_type',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='discount', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='discount', ctx=Load()),
                                            ops=[Gt()],
                                            comparators=[Constant(value=0, kind=None)],
                                        ),
                                        body=Constant(value='SC', kind=None),
                                        orelse=Constant(value='MG', kind=None),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='format_phone',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='number', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='number', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='number', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='number', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=' ', kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='/', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='.', kind=None),
                                            Constant(value='', kind=None),
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
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='number', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=4, kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='number', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Lt()],
                                                comparators=[Constant(value=13, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='number', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_vat_number',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='vat', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='vat', ctx=Load()),
                                                slice=Slice(
                                                    lower=Constant(value=2, kind=None),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=' ', kind=None),
                                            Constant(value='', kind=None),
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
                            name='get_vat_country',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='vat', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='vat', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=2, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='upper',
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
                            name='in_eu',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='partner', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='europe', ctx=Store())],
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
                                        args=[Constant(value='base.europe', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='country', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='country_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='europe', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='country', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Name(id='country', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='europe', ctx=Load()),
                                                        attr='country_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='formato_trasmissione', ctx=Store())],
                            value=Constant(value='FPR12', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='commercial_partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='l10n_it_pa_index',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='1', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=6, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='formato_trasmissione', ctx=Store())],
                                    value=Constant(value='FPA12', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='move_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='out_invoice', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='document_type', ctx=Store())],
                                    value=Constant(value='TD01', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='move_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='out_refund', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='document_type', ctx=Store())],
                                            value=Constant(value='TD04', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='document_type', ctx=Store())],
                                            value=Constant(value='TD0X', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='pdf', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
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
                                            args=[Constant(value='account.account_invoices', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='_render_qweb_pdf',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pdf', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pdf', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pdf_name', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='re', ctx=Load()),
                                        attr='sub',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='\\W+', kind=None),
                                        Constant(value='', kind=None),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Constant(value='.pdf', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_map', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                For(
                                    target=Name(id='tax', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='tax_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='tax', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0.0, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='tax_map', ctx=Load()),
                                                            slice=Name(id='tax', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='tax_map', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='tax', ctx=Load()),
                                                                Constant(value=0.0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='price_subtotal',
                                                            ctx=Load(),
                                                        ),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='template_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='record', kind=None),
                                    Constant(value='format_date', kind=None),
                                    Constant(value='format_monetary', kind=None),
                                    Constant(value='format_numbers', kind=None),
                                    Constant(value='format_numbers_two', kind=None),
                                    Constant(value='format_phone', kind=None),
                                    Constant(value='discount_type', kind=None),
                                    Constant(value='get_vat_number', kind=None),
                                    Constant(value='get_vat_country', kind=None),
                                    Constant(value='in_eu', kind=None),
                                    Constant(value='abs', kind=None),
                                    Constant(value='formato_trasmissione', kind=None),
                                    Constant(value='document_type', kind=None),
                                    Constant(value='pdf', kind=None),
                                    Constant(value='pdf_name', kind=None),
                                    Constant(value='tax_map', kind=None),
                                ],
                                values=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='format_date', ctx=Load()),
                                    Name(id='format_monetary', ctx=Load()),
                                    Name(id='format_numbers', ctx=Load()),
                                    Name(id='format_numbers_two', ctx=Load()),
                                    Name(id='format_phone', ctx=Load()),
                                    Name(id='discount_type', ctx=Load()),
                                    Name(id='get_vat_number', ctx=Load()),
                                    Name(id='get_vat_country', ctx=Load()),
                                    Name(id='in_eu', ctx=Load()),
                                    Name(id='abs', ctx=Load()),
                                    Name(id='formato_trasmissione', ctx=Load()),
                                    Name(id='document_type', ctx=Load()),
                                    Name(id='pdf', ctx=Load()),
                                    Name(id='pdf_name', ctx=Load()),
                                    Name(id='tax_map', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='template_values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_export_as_xml',
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
                            value=Constant(value='DEPRECATED : this will be moved to AccountEdiFormat in a future version.\n        Create the xml file content.\n        :return: The XML content as str.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='template_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_fatturapa_export_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='l10n_it_edi.account_invoice_it_FatturaPA_export', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[Name(id='template_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='content', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='soft', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='posted', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='soft',
                                        value=Name(id='soft', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='posted', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='l10n_it_send_state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='to_send', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='move_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='out_invoice', kind=None),
                                                                Constant(value='out_refund', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='m', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='IT', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='send_pec_mail',
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
                        Return(
                            value=Name(id='posted', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='send_pec_mail',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='allowed_state', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='to_send', kind=None),
                                    Constant(value='invalid', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_it_mail_pec_server_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='l10n_it_mail_pec_server_id',
                                                ctx=Load(),
                                            ),
                                            attr='active',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='l10n_it_address_send_fatturapa',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Error when sending mail with E-Invoice: Your company must have a mail PEC server and must indicate the mail PEC that will send electronic invoice.', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='l10n_it_send_state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='invalid', kind=None),
                                    type_comment=None,
                                ),
                                Return(value=None),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='l10n_it_send_state',
                                    ctx=Load(),
                                ),
                                ops=[NotIn()],
                                comparators=[Name(id='allowed_state', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value="%s isn't in a right state. It must be in a 'Not yet send' or 'Invalid' state.", kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='display_name',
                                                    ctx=Load(),
                                                ),
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
                            targets=[Name(id='message', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subject', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='author_id', kind=None),
                                            Constant(value='email_from', kind=None),
                                            Constant(value='reply_to', kind=None),
                                            Constant(value='mail_server_id', kind=None),
                                            Constant(value='attachment_ids', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Sending file: %s', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='l10n_it_einvoice_name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Sending file: %s to ES: %s', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='l10n_it_einvoice_name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='company',
                                                                ctx=Load(),
                                                            ),
                                                            attr='l10n_it_address_recipient_fatturapa',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
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
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='l10n_it_address_send_fatturapa',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='l10n_it_address_send_fatturapa',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='l10n_it_mail_pec_server_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='l10n_it_einvoice_id',
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_fattura', ctx=Store())],
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
                                                        slice=Constant(value='mail.mail', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='wo_bounce_return_path',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='mail_message_id', kind=None),
                                            Constant(value='email_to', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='message', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='l10n_it_address_recipient_fatturapa',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mail_fattura', ctx=Load()),
                                            attr='send',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='raise_exception',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=BinOp(
                                                    left=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Mail sent on %s by %s', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Datetime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='now',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='user',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='display_name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='l10n_it_send_state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='sent', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='MailDeliveryException', ctx=Load()),
                                    name='error',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=BinOp(
                                                            left=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Error when sending mail with E-Invoice: %s', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            op=Mod(),
                                                            right=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='error', ctx=Load()),
                                                                    attr='args',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='l10n_it_send_state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='invalid', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compose_info_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                            arg(arg='element_tags', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='output_str', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='elements', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Name(id='element_tags', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='element', ctx=Store()),
                            iter=Name(id='elements', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='output_str', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='<ul>', kind=None),
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='element', ctx=Load()),
                                            attr='iter',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='text', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value=' ', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='split',
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
                                                If(
                                                    test=Name(id='text', ctx=Load()),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='output_str', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Constant(value='<li>%s: %s</li>', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='tag',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Name(id='text', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='output_str', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='</ul>', kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='output_str', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compose_multi_info_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tree', annotation=None, type_comment=None),
                            arg(arg='element_tags', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='output_str', ctx=Store())],
                            value=Constant(value='<ul>', kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='element_tag', ctx=Store()),
                            iter=Name(id='element_tags', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='elements', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tree', ctx=Load()),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='element_tag', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='elements', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='element', ctx=Store()),
                                    iter=Name(id='elements', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='text', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value=' ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='element', ctx=Load()),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
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
                                        If(
                                            test=Name(id='text', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='output_str', ctx=Store()),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Constant(value='<li>%s: %s</li>', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='tag',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='text', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='output_str', ctx=Load()),
                                op=Add(),
                                right=Constant(value='</ul>', kind=None),
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
        ClassDef(
            name='AccountTax',
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
                    value=Constant(value='account.tax', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='account.tax', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_vat_due_date', ctx=Store())],
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
                                            Constant(value='I', kind=None),
                                            Constant(value='[I] IVA ad esigibilità immediata', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='D', kind=None),
                                            Constant(value='[D] IVA ad esigibilità differita', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='S', kind=None),
                                            Constant(value='[S] Scissione dei pagamenti', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='I', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='VAT due date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_has_exoneration', ctx=Store())],
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
                                value=Constant(value='Has exoneration of tax (Italy)', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Tax has a tax exoneration.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_kind_exoneration', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='N1', kind=None),
                                                Constant(value='[N1] Escluse ex art. 15', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N2', kind=None),
                                                Constant(value='[N2] Non soggette', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N2.1', kind=None),
                                                Constant(value='[N2.1] Non soggette ad IVA ai sensi degli artt. Da 7 a 7-septies del DPR 633/72', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N2.2', kind=None),
                                                Constant(value='[N2.2] Non soggette – altri casi', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N3', kind=None),
                                                Constant(value='[N3] Non imponibili', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N3.1', kind=None),
                                                Constant(value='[N3.1] Non imponibili – esportazioni', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N3.2', kind=None),
                                                Constant(value='[N3.2] Non imponibili – cessioni intracomunitarie', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N3.3', kind=None),
                                                Constant(value='[N3.3] Non imponibili – cessioni verso San Marino', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N3.4', kind=None),
                                                Constant(value='[N3.4] Non imponibili – operazioni assimilate alle cessioni all’esportazione', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N3.5', kind=None),
                                                Constant(value='[N3.5] Non imponibili – a seguito di dichiarazioni d’intento', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N3.6', kind=None),
                                                Constant(value='[N3.6] Non imponibili – altre operazioni che non concorrono alla formazione del plafond', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N4', kind=None),
                                                Constant(value='[N4] Esenti', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N5', kind=None),
                                                Constant(value='[N5] Regime del margine / IVA non esposta in fattura', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6', kind=None),
                                                Constant(value='[N6] Inversione contabile (per le operazioni in reverse charge ovvero nei casi di autofatturazione per acquisti extra UE di servizi ovvero per importazioni di beni nei soli casi previsti)', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.1', kind=None),
                                                Constant(value='[N6.1] Inversione contabile – cessione di rottami e altri materiali di recupero', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.2', kind=None),
                                                Constant(value='[N6.2] Inversione contabile – cessione di oro e argento puro', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.3', kind=None),
                                                Constant(value='[N6.3] Inversione contabile – subappalto nel settore edile', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.4', kind=None),
                                                Constant(value='[N6.4] Inversione contabile – cessione di fabbricati', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.5', kind=None),
                                                Constant(value='[N6.5] Inversione contabile – cessione di telefoni cellulari', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.6', kind=None),
                                                Constant(value='[N6.6] Inversione contabile – cessione di prodotti elettronici', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.7', kind=None),
                                                Constant(value='[N6.7] Inversione contabile – prestazioni comparto edile esettori connessi', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.8', kind=None),
                                                Constant(value='[N6.8] Inversione contabile – operazioni settore energetico', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N6.9', kind=None),
                                                Constant(value='[N6.9] Inversione contabile – altri casi', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='N7', kind=None),
                                                Constant(value='[N7] IVA assolta in altro stato UE (vendite a distanza ex art. 40 c. 3 e 4 e art. 41 c. 1 lett. b,  DL 331/93; prestazione di servizi di telecomunicazioni, tele-radiodiffusione ed elettronici ex art. 7-sexies lett. f, g, art. 74-sexies DPR 633/72)', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Exoneration', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Exoneration type', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='N1', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_it_law_reference', ctx=Store())],
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
                                value=Constant(value='Law Reference', kind=None),
                            ),
                            keyword(
                                arg='size',
                                value=Constant(value=100, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_exoneration_with_no_tax',
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
                            target=Name(id='tax', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='tax', ctx=Load()),
                                        attr='l10n_it_has_exoneration',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='tax', ctx=Load()),
                                                            attr='l10n_it_kind_exoneration',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='tax', ctx=Load()),
                                                            attr='l10n_it_law_reference',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='tax', ctx=Load()),
                                                            attr='amount',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='If the tax has exoneration, you must enter a kind of exoneration, a law reference and the amount of the tax must be 0.0.', kind=None)],
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
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='tax', ctx=Load()),
                                                            attr='l10n_it_kind_exoneration',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='N6', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='tax', ctx=Load()),
                                                            attr='l10n_it_vat_due_date',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='S', kind=None)],
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
                                                                args=[Constant(value="'Scissione dei pagamenti' is not compatible with exoneration of kind 'N6'", kind=None)],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='l10n_it_has_exoneration', kind=None),
                                Constant(value='l10n_it_kind_exoneration', kind=None),
                                Constant(value='l10n_it_law_reference', kind=None),
                                Constant(value='amount', kind=None),
                                Constant(value='l10n_it_vat_due_date', kind=None),
                            ],
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
