Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
                alias(name='_lt', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.account_edi_proxy_client.models.account_edi_proxy_user',
            names=[
                alias(name='AccountEdiProxyError', asname=None),
                alias(name='DEFAULT_SERVER_URL', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
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
            name='AccountEdiFormat',
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
                    value=Constant(value='account.edi.format', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_cron_receive_fattura_pa',
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
                            value=Constant(value=' Check the proxy for incoming invoices.\n        ', kind=None),
                        ),
                        If(
                            test=Call(
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.demo', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='server_url', ctx=Store())],
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.edi_server_url', kind=None),
                                    Name(id='DEFAULT_SERVER_URL', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='proxy_users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account_edi_proxy_client.user', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='edi_format_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
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
                        For(
                            target=Name(id='proxy_user', ctx=Store()),
                            iter=Name(id='proxy_users', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='proxy_user', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='proxy_user', ctx=Load()),
                                                    attr='_make_request',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='server_url', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value='/api/l10n_it_edi/1/in/RicezioneInvoice', kind=None),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='params',
                                                        value=Dict(
                                                            keys=[Constant(value='recipient_codice_fiscale', kind=None)],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='company', ctx=Load()),
                                                                    attr='l10n_it_codice_fiscale',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='AccountEdiProxyError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Error while receiving file from SdiCoop: %s', kind=None),
                                                            Name(id='e', ctx=Load()),
                                                        ],
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
                                    targets=[Name(id='proxy_acks', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='id_transaction', ctx=Store()),
                                            Name(id='fattura', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
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
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Subscript(
                                                                        value=Name(id='fattura', ctx=Load()),
                                                                        slice=Constant(value='filename', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='res_model', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='account.move', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='limit',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='E-invoice already exist: %s', kind=None),
                                                            Subscript(
                                                                value=Name(id='fattura', ctx=Load()),
                                                                slice=Constant(value='filename', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='proxy_acks', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='id_transaction', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='file', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='proxy_user', ctx=Load()),
                                                    attr='_decrypt_data',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='fattura', ctx=Load()),
                                                        slice=Constant(value='file', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='fattura', ctx=Load()),
                                                        slice=Constant(value='key', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tree', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='fromstring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='file', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Received file badly formatted, skipping: \n %s', kind=None),
                                                                    Name(id='file', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Continue(),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='invoice', ctx=Store())],
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
                                                        args=[Constant(value='l10n_it_edi.edi_fatturaPA', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='_create_invoice_from_xml_tree',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='fattura', ctx=Load()),
                                                        slice=Constant(value='filename', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='tree', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
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
                                                            Constant(value='raw', kind=None),
                                                            Constant(value='type', kind=None),
                                                            Constant(value='res_model', kind=None),
                                                            Constant(value='res_id', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='fattura', ctx=Load()),
                                                                slice=Constant(value='filename', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='file', ctx=Load()),
                                                            Constant(value='binary', kind=None),
                                                            Constant(value='account.move', kind=None),
                                                            Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='proxy_acks', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='id_transaction', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='proxy_acks', ctx=Load()),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='proxy_user', ctx=Load()),
                                                            attr='_make_request',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='server_url', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value='/api/l10n_it_edi/1/ack', kind=None),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='params',
                                                                value=Dict(
                                                                    keys=[Constant(value='transaction_ids', kind=None)],
                                                                    values=[Name(id='proxy_acks', ctx=Load())],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='AccountEdiProxyError', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='error',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Error while receiving file from SdiCoop: %s', kind=None),
                                                                    Name(id='e', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_move_configuration',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move', annotation=None, type_comment=None),
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_check_move_configuration',
                                    ctx=Load(),
                                ),
                                args=[Name(id='move', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='fattura_pa', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_l10n_it_edi_check_invoice_configuration',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='move', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_proxy_user',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You must accept the terms and conditions in the settings to use FatturaPA.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_needs_web_services',
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
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='fattura_pa', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_needs_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                    name='_l10n_it_edi_is_required_for_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' _is_required_for_invoice for SdiCoop.\n            OVERRIDE\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='country_code',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='IT', kind=None)],
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
                    name='_support_batching',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move', annotation=None, type_comment=None),
                            arg(arg='state', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='fattura_pa', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='state', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='to_send', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='is_invoice',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
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
                                    attr='_support_batching',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='move',
                                        value=Name(id='move', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='state',
                                        value=Name(id='state', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='company',
                                        value=Name(id='company', ctx=Load()),
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
                    name='_l10n_it_post_invoices_step_1',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoices', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Send the invoices to the proxy.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='to_return', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_send', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice', ctx=Store()),
                            iter=Name(id='invoices', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='xml', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value="<?xml version='1.0' encoding='UTF-8'?>", kind=None),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
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
                                    targets=[Name(id='filename', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_l10n_it_edi_generate_electronic_invoice_filename',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoice', ctx=Load())],
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
                                                    Name(id='filename', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='xml', ctx=Load()),
                                                            attr='encode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Italian invoice: %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='move_type',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='binary', kind=None),
                                                ],
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
                                            attr='l10n_it_edi_attachment_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='attachment', ctx=Load()),
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
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='commercial_partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='l10n_it_pa_index',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=6, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Invoices for PA are not managed by Odoo, you can download the document and send it on your own.', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='to_return', ctx=Load()),
                                                    slice=Name(id='invoice', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[Constant(value='attachment', kind=None)],
                                                values=[Name(id='attachment', ctx=Load())],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='to_send', ctx=Load()),
                                                    slice=Name(id='filename', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='invoice', kind=None),
                                                    Constant(value='data', kind=None),
                                                ],
                                                values=[
                                                    Name(id='invoice', ctx=Load()),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='filename', kind=None),
                                                            Constant(value='xml', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='filename', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='base64', ctx=Load()),
                                                                            attr='b64encode',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='xml', ctx=Load()),
                                                                                    attr='encode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='decode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoices', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='proxy_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_proxy_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='company', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='proxy_user', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=DictComp(
                                        key=Name(id='invoice', ctx=Load()),
                                        value=Dict(
                                            keys=[
                                                Constant(value='error', kind=None),
                                                Constant(value='blocking_level', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='You must accept the terms and conditions in the settings to use FatturaPA.', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='error', kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='invoice', ctx=Store()),
                                                iter=Name(id='invoices', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.demo', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='responses', ctx=Store())],
                                    value=DictComp(
                                        key=Name(id='filename', ctx=Load()),
                                        value=Dict(
                                            keys=[Constant(value='id_transaction', kind=None)],
                                            values=[Constant(value='demo', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='invoice', ctx=Store()),
                                                iter=Name(id='invoices', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='responses', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_l10n_it_edi_upload',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=Subscript(
                                                            value=Name(id='i', ctx=Load()),
                                                            slice=Constant(value='data', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='i', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='to_send', ctx=Load()),
                                                                        attr='values',
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
                                                    Name(id='proxy_user', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='AccountEdiProxyError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Return(
                                                    value=DictComp(
                                                        key=Name(id='invoice', ctx=Load()),
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='error', kind=None),
                                                                Constant(value='blocking_level', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    attr='message',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='error', kind=None),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='invoice', ctx=Store()),
                                                                iter=Name(id='invoices', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='filename', ctx=Store()),
                                    Name(id='response', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='responses', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='to_send', ctx=Load()),
                                            slice=Name(id='filename', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='invoice', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='to_return', ctx=Load()),
                                            slice=Name(id='invoice', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='response', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='id_transaction', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='response', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='l10n_it_edi_transaction',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='response', ctx=Load()),
                                                slice=Constant(value='id_transaction', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='to_return', ctx=Load()),
                                                        slice=Name(id='invoice', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='error', kind=None),
                                                            Constant(value='blocking_level', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='The invoice was successfully transmitted to the Public Administration and we are waiting for confirmation.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='info', kind=None),
                                                        ],
                                                    ),
                                                ],
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
                            value=Name(id='to_return', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_l10n_it_post_invoices_step_2',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoices', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check if the sent invoices have been processed by FatturaPA.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='server_url', ctx=Store())],
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.edi_server_url', kind=None),
                                    Name(id='DEFAULT_SERVER_URL', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_check', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='i', ctx=Load()),
                                    attr='l10n_it_edi_transaction',
                                    ctx=Load(),
                                ),
                                value=Name(id='i', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Name(id='invoices', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_return', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Attribute(
                                value=Name(id='invoices', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='proxy_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_proxy_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='company', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='proxy_user', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=DictComp(
                                        key=Name(id='invoice', ctx=Load()),
                                        value=Dict(
                                            keys=[
                                                Constant(value='error', kind=None),
                                                Constant(value='blocking_level', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='You must accept the terms and conditions in the settings to use FatturaPA.', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='error', kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='invoice', ctx=Store()),
                                                iter=Name(id='invoices', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.demo', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=DictComp(
                                        key=Name(id='invoice', ctx=Load()),
                                        value=Dict(
                                            keys=[Constant(value='attachment', kind=None)],
                                            values=[
                                                Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='l10n_it_edi_attachment_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='invoice', ctx=Store()),
                                                iter=Name(id='invoices', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='responses', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='proxy_user', ctx=Load()),
                                                    attr='_make_request',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='server_url', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value='/api/l10n_it_edi/1/in/TrasmissioneFatture', kind=None),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='params',
                                                        value=Dict(
                                                            keys=[Constant(value='ids_transaction', kind=None)],
                                                            values=[
                                                                Call(
                                                                    func=Name(id='list', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='to_check', ctx=Load()),
                                                                                attr='keys',
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
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='AccountEdiProxyError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Return(
                                                    value=DictComp(
                                                        key=Name(id='invoice', ctx=Load()),
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='error', kind=None),
                                                                Constant(value='blocking_level', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    attr='message',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value='error', kind=None),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='invoice', ctx=Store()),
                                                                iter=Name(id='invoices', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='proxy_acks', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='id_transaction', ctx=Store()),
                                    Name(id='response', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='responses', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='to_check', ctx=Load()),
                                        slice=Name(id='id_transaction', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='error', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='response', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='to_return', ctx=Load()),
                                                    slice=Name(id='invoice', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='response', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='state', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='response', ctx=Load()),
                                        slice=Constant(value='state', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='state', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='awaiting_outcome', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='to_return', ctx=Load()),
                                                    slice=Name(id='invoice', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='error', kind=None),
                                                    Constant(value='blocking_level', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The invoice was successfully transmitted to the Public Administration and we are waiting for confirmation', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='info', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='proxy_acks', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='id_transaction', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='state', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='not_found', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='to_return', ctx=Load()),
                                                            slice=Name(id='invoice', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='error', kind=None),
                                                            Constant(value='blocking_level', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='You are not allowed to check the status of this invoice.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='error', kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='xml', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='proxy_user', ctx=Load()),
                                            attr='_decrypt_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='response', ctx=Load()),
                                                slice=Constant(value='file', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='response', ctx=Load()),
                                                slice=Constant(value='key', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='response_tree', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='xml', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='state', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='ricevutaConsegna', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='to_return', ctx=Load()),
                                                    slice=Name(id='invoice', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[Constant(value='error', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The invoice has been succesfully transmitted. The addressee has 15 days to accept or reject it.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='state', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='notificaScarto', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='errors', ctx=Store())],
                                                    value=ListComp(
                                                        elt=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='element', ctx=Load()),
                                                                    attr='find',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='Descrizione', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='element', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='response_tree', ctx=Load()),
                                                                        attr='xpath',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='//Errore', kind=None)],
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
                                                            value=Name(id='to_return', ctx=Load()),
                                                            slice=Name(id='invoice', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='error', kind=None),
                                                            Constant(value='blocking_level', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_format_error_message',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='The invoice has been refused by the Exchange System', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='errors', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='error', kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='state', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='notificaMancataConsegna', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='to_return', ctx=Load()),
                                                                    slice=Name(id='invoice', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Dict(
                                                                keys=[Constant(value='error', kind=None)],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='The E-invoice is not delivered to the addressee. The Exchange System is                    unable to deliver the file to the Public Administration. The Exchange System will                    contact the PA to report the problem and request that they provide a solution.                     During the following 15 days, the Exchange System will try to forward the FatturaPA                    file to the Administration in question again.', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='state', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='notificaEsito', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='outcome', ctx=Store())],
                                                                    value=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='response_tree', ctx=Load()),
                                                                                attr='find',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='Esito', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='text',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='outcome', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='EC01', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='to_return', ctx=Load()),
                                                                                    slice=Name(id='invoice', ctx=Load()),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Dict(
                                                                                keys=[
                                                                                    Constant(value='attachment', kind=None),
                                                                                    Constant(value='success', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Name(id='invoice', ctx=Load()),
                                                                                        attr='l10n_it_edi_attachment_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=True, kind=None),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='to_return', ctx=Load()),
                                                                                    slice=Name(id='invoice', ctx=Load()),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Dict(
                                                                                keys=[
                                                                                    Constant(value='error', kind=None),
                                                                                    Constant(value='blocking_level', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[Constant(value='The invoice was refused by the addressee.', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    Constant(value='error', kind=None),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='state', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='NotificaDecorrenzaTermini', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='to_return', ctx=Load()),
                                                                                    slice=Name(id='invoice', ctx=Load()),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Dict(
                                                                                keys=[
                                                                                    Constant(value='error', kind=None),
                                                                                    Constant(value='blocking_level', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[Constant(value='Expiration of the maximum term for communication of acceptance/refusal', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    Constant(value='error', kind=None),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='proxy_acks', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='id_transaction', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='proxy_user', ctx=Load()),
                                            attr='_make_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='server_url', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value='/api/l10n_it_edi/1/ack', kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='params',
                                                value=Dict(
                                                    keys=[Constant(value='transaction_ids', kind=None)],
                                                    values=[Name(id='proxy_acks', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccountEdiProxyError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Error while acking file to SdiCoop: %s', kind=None),
                                                    Name(id='e', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='to_return', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_fattura_pa',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoices', annotation=None, type_comment=None),
                        ],
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
                                operand=Attribute(
                                    value=Name(id='invoices', ctx=Load()),
                                    attr='l10n_it_edi_transaction',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_l10n_it_post_invoices_step_1',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoices', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_l10n_it_post_invoices_step_2',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoices', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_proxy_identification',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
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
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='fattura_pa', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_get_proxy_identification',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='company', ctx=Load()),
                                    attr='l10n_it_codice_fiscale',
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
                                                args=[Constant(value='Please fill your codice fiscale to be able to receive invoices from FatturaPA', kind=None)],
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
                        Return(
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
                                    attr='_l10n_it_normalize_codice_fiscale',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='l10n_it_codice_fiscale',
                                        ctx=Load(),
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
                    name='_l10n_it_edi_upload',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='files', annotation=None, type_comment=None),
                            arg(arg='proxy_user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Upload files to fatturapa.\n\n        :param files:    A list of dictionary {filename, base64_xml}.\n        :returns:        A dictionary.\n        * message:       Message from fatturapa.\n        * transactionId: The fatturapa ID of this request.\n        * error:         An eventual error.\n        * error_level:   Info, warning, error.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ERRORS', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='EI01', kind=None),
                                    Constant(value='EI02', kind=None),
                                    Constant(value='EI03', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='error', kind=None),
                                            Constant(value='blocking_level', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_lt', ctx=Load()),
                                                args=[Constant(value='Attached file is empty', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='error', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='error', kind=None),
                                            Constant(value='blocking_level', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_lt', ctx=Load()),
                                                args=[Constant(value='Service momentarily unavailable', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='warning', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='error', kind=None),
                                            Constant(value='blocking_level', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_lt', ctx=Load()),
                                                args=[Constant(value='Unauthorized user', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='error', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='server_url', ctx=Store())],
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
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_proxy_client.edi_server_url', kind=None),
                                    Name(id='DEFAULT_SERVER_URL', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='proxy_user', ctx=Load()),
                                    attr='_make_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='server_url', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value='/api/l10n_it_edi/1/out/SdiRiceviFile', kind=None),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[Constant(value='files', kind=None)],
                                            values=[Name(id='files', ctx=Load())],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='filename', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='keys',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='error', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Name(id='filename', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Name(id='filename', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ERRORS', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Name(id='filename', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='error', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='error', kind=None),
                                                            Constant(value='blocking_level', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='result', ctx=Load()),
                                                                    slice=Name(id='filename', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='error', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='error', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
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
                        Return(
                            value=Name(id='result', ctx=Load()),
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
