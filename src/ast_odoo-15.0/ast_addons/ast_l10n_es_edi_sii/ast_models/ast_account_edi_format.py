Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='urllib3.util.ssl_',
            names=[
                alias(name='create_urllib3_context', asname=None),
                alias(name='DEFAULT_CIPHERS', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='OpenSSL.crypto',
            names=[
                alias(name='load_certificate', asname=None),
                alias(name='load_privatekey', asname=None),
                alias(name='FILETYPE_PEM', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='zeep.transports',
            names=[alias(name='Transport', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='html_escape', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='math', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='zeep', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='EUSKADI_CIPHERS', ctx=Store())],
            value=JoinedStr(
                values=[
                    FormattedValue(
                        value=Name(id='DEFAULT_CIPHERS', ctx=Load()),
                        conversion=-1,
                        format_spec=None,
                    ),
                    Constant(value=':!DH', kind=None),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='PatchedHTTPAdapter',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='requests', ctx=Load()),
                        attr='adapters',
                        ctx=Load(),
                    ),
                    attr='HTTPAdapter',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' An adapter to block DH ciphers which may not work for the tax agencies called', kind=None),
                ),
                FunctionDef(
                    name='init_poolmanager',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='kwargs', ctx=Load()),
                                    slice=Constant(value='ssl_context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='create_urllib3_context', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='ciphers',
                                        value=Name(id='EUSKADI_CIPHERS', ctx=Load()),
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='init_poolmanager',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
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
                    name='cert_verify',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='conn', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='verify', annotation=None, type_comment=None),
                            arg(arg='cert', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='cert_verify',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='conn', ctx=Load()),
                                    Name(id='url', ctx=Load()),
                                    Name(id='verify', ctx=Load()),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='conn', ctx=Load()),
                                    attr='cert_file',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='cert', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='conn', ctx=Load()),
                                    attr='key_file',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='cert', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_connection',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='proxies', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='conn', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_connection',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='proxies',
                                        value=Name(id='proxies', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='conn', ctx=Load()),
                                    attr='conn_kw',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ssl_context', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='patched_load_cert_chain',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='l10n_es_odoo_certificate', annotation=None, type_comment=None),
                                    arg(arg='keyfile', annotation=None, type_comment=None),
                                    arg(arg='password', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='cert_file', ctx=Store()),
                                                Name(id='key_file', ctx=Store()),
                                                Name(id='dummy', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='l10n_es_odoo_certificate', ctx=Load()),
                                            attr='_decode_certificate',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='cert_obj', ctx=Store())],
                                    value=Call(
                                        func=Name(id='load_certificate', ctx=Load()),
                                        args=[
                                            Name(id='FILETYPE_PEM', ctx=Load()),
                                            Name(id='cert_file', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pkey_obj', ctx=Store())],
                                    value=Call(
                                        func=Name(id='load_privatekey', ctx=Load()),
                                        args=[
                                            Name(id='FILETYPE_PEM', ctx=Load()),
                                            Name(id='key_file', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='context', ctx=Load()),
                                                attr='_ctx',
                                                ctx=Load(),
                                            ),
                                            attr='use_certificate',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cert_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='context', ctx=Load()),
                                                attr='_ctx',
                                                ctx=Load(),
                                            ),
                                            attr='use_privatekey',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pkey_obj', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='load_cert_chain',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='patched_load_cert_chain', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='conn', ctx=Load()),
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
                    name='_l10n_es_edi_get_invoices_tax_details_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                            arg(arg='filter_invl_to_apply', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        FunctionDef(
                            name='grouping_key_generator',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='tax_values', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='tax', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='tax_values', ctx=Load()),
                                        slice=Constant(value='tax_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='applied_tax_amount', kind=None),
                                            Constant(value='l10n_es_type', kind=None),
                                            Constant(value='l10n_es_exempt_reason', kind=None),
                                            Constant(value='l10n_es_bien_inversion', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='tax', ctx=Load()),
                                                attr='amount',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='tax', ctx=Load()),
                                                attr='l10n_es_type',
                                                ctx=Load(),
                                            ),
                                            IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Name(id='tax', ctx=Load()),
                                                        attr='l10n_es_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='exento', kind=None)],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='tax', ctx=Load()),
                                                    attr='l10n_es_exempt_reason',
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                            Attribute(
                                                value=Name(id='tax', ctx=Load()),
                                                attr='l10n_es_bien_inversion',
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
                            name='filter_to_apply',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='tax_values', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Compare(
                                        left=Attribute(
                                            value=Subscript(
                                                value=Name(id='tax_values', ctx=Load()),
                                                slice=Constant(value='tax_repartition_line_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='factor_percent',
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0.0, kind=None)],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='full_filter_invl_to_apply',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='invoice_line', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='ignore', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='invoice_line', ctx=Load()),
                                                                attr='tax_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='flatten_taxes_hierarchy',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='l10n_es_type', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=IfExp(
                                        test=Name(id='filter_invl_to_apply', ctx=Load()),
                                        body=Call(
                                            func=Name(id='filter_invl_to_apply', ctx=Load()),
                                            args=[Name(id='invoice_line', ctx=Load())],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=True, kind=None),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_details', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='_prepare_edi_tax_details',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='grouping_key_generator',
                                        value=Name(id='grouping_key_generator', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='filter_invl_to_apply',
                                        value=Name(id='full_filter_invl_to_apply', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='filter_to_apply',
                                        value=Name(id='filter_to_apply', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sign', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='is_sale_document',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                body=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                orelse=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_details_info', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='dict', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recargo_tax_details', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='invoice_line_ids',
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
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='display_type',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='filter_invl_to_apply', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='invoice_lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoice_lines', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='filter_invl_to_apply', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='invoice_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='taxes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='tax_ids',
                                                ctx=Load(),
                                            ),
                                            attr='flatten_taxes_hierarchy',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='recargo_tax', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='t', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='t', ctx=Store()),
                                                iter=Name(id='taxes', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='t', ctx=Load()),
                                                            attr='l10n_es_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='recargo', kind=None)],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='recargo_tax', ctx=Load()),
                                            Name(id='taxes', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='recargo_main_tax', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='taxes', ctx=Load()),
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
                                                            body=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='l10n_es_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='sujeto', kind=None),
                                                                            Constant(value='sujeto_isp', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=1, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='recargo_tax_details', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='recargo_main_tax', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='recargo_tax_details', ctx=Load()),
                                                            slice=Name(id='recargo_main_tax', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=ListComp(
                                                            elt=Name(id='x', ctx=Load()),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='x', ctx=Store()),
                                                                    iter=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='tax_details', ctx=Load()),
                                                                                slice=Constant(value='tax_details', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='values',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    ifs=[
                                                                        Compare(
                                                                            left=Subscript(
                                                                                value=Subscript(
                                                                                    value=Subscript(
                                                                                        value=Name(id='x', ctx=Load()),
                                                                                        slice=Constant(value='group_tax_details', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='tax_id', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[
                                                                                Subscript(
                                                                                    value=Name(id='recargo_tax', ctx=Load()),
                                                                                    slice=Constant(value=0, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
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
                        Assign(
                            targets=[Name(id='tax_amount_deductible', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_amount_retention', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_amount_not_subject', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_amount_not_subject_loc', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_subject_info_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tax_subject_isp_info_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='tax_values', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='tax_details', ctx=Load()),
                                        slice=Constant(value='tax_details', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='tax_values', ctx=Load()),
                                                    slice=Constant(value='l10n_es_type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='sujeto', kind=None),
                                                            Constant(value='sujeto_isp', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='tax_amount_deductible', ctx=Store()),
                                                    op=Add(),
                                                    value=Subscript(
                                                        value=Name(id='tax_values', ctx=Load()),
                                                        slice=Constant(value='tax_amount', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='base_amount', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='sign', ctx=Load()),
                                                        op=Mult(),
                                                        right=Subscript(
                                                            value=Name(id='tax_values', ctx=Load()),
                                                            slice=Constant(value='base_amount', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='tax_info', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='TipoImpositivo', kind=None),
                                                            Constant(value='BaseImponible', kind=None),
                                                            Constant(value='CuotaRepercutida', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='tax_values', ctx=Load()),
                                                                slice=Constant(value='applied_tax_amount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='round', ctx=Load()),
                                                                args=[
                                                                    Name(id='base_amount', ctx=Load()),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='round', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='math', ctx=Load()),
                                                                            attr='copysign',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='tax_values', ctx=Load()),
                                                                                slice=Constant(value='tax_amount', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='base_amount', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='recargo', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='recargo_tax_details', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tax_values', ctx=Load()),
                                                                        slice=Constant(value='group_tax_details', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='tax_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='recargo', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='tax_info', ctx=Load()),
                                                                    slice=Constant(value='CuotaRecargoEquivalencia', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Name(id='round', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='sign', ctx=Load()),
                                                                        op=Mult(),
                                                                        right=Subscript(
                                                                            value=Name(id='recargo', ctx=Load()),
                                                                            slice=Constant(value='tax_amount', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='tax_info', ctx=Load()),
                                                                    slice=Constant(value='TipoRecargoEquivalencia', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='recargo', ctx=Load()),
                                                                slice=Constant(value='applied_tax_amount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='tax_values', ctx=Load()),
                                                            slice=Constant(value='l10n_es_type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='sujeto', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='tax_subject_info_list', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='tax_info', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='tax_subject_isp_info_list', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='tax_info', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='tax_values', ctx=Load()),
                                                            slice=Constant(value='l10n_es_type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='exento', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='tax_details_info', ctx=Load()),
                                                                        slice=Constant(value='Sujeta', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='setdefault',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Exenta', kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleExenta', kind=None)],
                                                                        values=[List(elts=[], ctx=Load())],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Subscript(
                                                                            value=Subscript(
                                                                                value=Name(id='tax_details_info', ctx=Load()),
                                                                                slice=Constant(value='Sujeta', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='Exenta', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='DetalleExenta', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='BaseImponible', kind=None),
                                                                            Constant(value='CausaExencion', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Call(
                                                                                func=Name(id='round', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Name(id='sign', ctx=Load()),
                                                                                        op=Mult(),
                                                                                        right=Subscript(
                                                                                            value=Name(id='tax_values', ctx=Load()),
                                                                                            slice=Constant(value='base_amount', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    Constant(value=2, kind=None),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            Subscript(
                                                                                value=Name(id='tax_values', ctx=Load()),
                                                                                slice=Constant(value='l10n_es_exempt_reason', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='tax_values', ctx=Load()),
                                                                    slice=Constant(value='l10n_es_type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='retencion', kind=None)],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='tax_amount_retention', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Subscript(
                                                                        value=Name(id='tax_values', ctx=Load()),
                                                                        slice=Constant(value='tax_amount', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='tax_values', ctx=Load()),
                                                                            slice=Constant(value='l10n_es_type', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='no_sujeto', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Name(id='base_amount_not_subject', ctx=Store()),
                                                                            op=Add(),
                                                                            value=Subscript(
                                                                                value=Name(id='tax_values', ctx=Load()),
                                                                                slice=Constant(value='base_amount', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Subscript(
                                                                                    value=Name(id='tax_values', ctx=Load()),
                                                                                    slice=Constant(value='l10n_es_type', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='no_sujeto_loc', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                AugAssign(
                                                                                    target=Name(id='base_amount_not_subject_loc', ctx=Store()),
                                                                                    op=Add(),
                                                                                    value=Subscript(
                                                                                        value=Name(id='tax_values', ctx=Load()),
                                                                                        slice=Constant(value='base_amount', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Subscript(
                                                                                            value=Name(id='tax_values', ctx=Load()),
                                                                                            slice=Constant(value='l10n_es_type', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='ignore', kind=None)],
                                                                                    ),
                                                                                    body=[Continue()],
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
                                            ],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='tax_subject_isp_info_list', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='tax_subject_info_list', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='tax_details_info', ctx=Load()),
                                                                slice=Constant(value='Sujeta', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='NoExenta', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[Constant(value='TipoNoExenta', kind=None)],
                                                        values=[Constant(value='S2', kind=None)],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='tax_subject_isp_info_list', ctx=Load()),
                                                            ),
                                                            Name(id='tax_subject_info_list', ctx=Load()),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tax_details_info', ctx=Load()),
                                                                        slice=Constant(value='Sujeta', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='NoExenta', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Dict(
                                                                keys=[Constant(value='TipoNoExenta', kind=None)],
                                                                values=[Constant(value='S1', kind=None)],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='tax_subject_isp_info_list', ctx=Load()),
                                                                    Name(id='tax_subject_info_list', ctx=Load()),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Subscript(
                                                                                value=Name(id='tax_details_info', ctx=Load()),
                                                                                slice=Constant(value='Sujeta', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='NoExenta', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Dict(
                                                                        keys=[Constant(value='TipoNoExenta', kind=None)],
                                                                        values=[Constant(value='S3', kind=None)],
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
                                        If(
                                            test=Name(id='tax_subject_info_list', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='tax_details_info', ctx=Load()),
                                                                    slice=Constant(value='Sujeta', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='NoExenta', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='DesgloseIVA', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tax_details_info', ctx=Load()),
                                                                        slice=Constant(value='Sujeta', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='NoExenta', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='DesgloseIVA', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='DetalleIVA', kind=None),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Subscript(
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='tax_details_info', ctx=Load()),
                                                                    slice=Constant(value='Sujeta', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='NoExenta', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='DesgloseIVA', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='DetalleIVA', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Name(id='tax_subject_info_list', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='tax_subject_isp_info_list', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='tax_details_info', ctx=Load()),
                                                                    slice=Constant(value='Sujeta', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='NoExenta', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='DesgloseIVA', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tax_details_info', ctx=Load()),
                                                                        slice=Constant(value='Sujeta', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='NoExenta', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='DesgloseIVA', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='DetalleIVA', kind=None),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Subscript(
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='tax_details_info', ctx=Load()),
                                                                    slice=Constant(value='Sujeta', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='NoExenta', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='DesgloseIVA', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='DetalleIVA', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Name(id='tax_subject_isp_info_list', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='tax_values', ctx=Load()),
                                                    slice=Constant(value='l10n_es_type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='sujeto', kind=None),
                                                            Constant(value='sujeto_isp', kind=None),
                                                            Constant(value='no_sujeto', kind=None),
                                                            Constant(value='no_sujeto_loc', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='tax_amount_deductible', ctx=Store()),
                                                    op=Add(),
                                                    value=Subscript(
                                                        value=Name(id='tax_values', ctx=Load()),
                                                        slice=Constant(value='tax_amount', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='tax_values', ctx=Load()),
                                                            slice=Constant(value='l10n_es_type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='retencion', kind=None)],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='tax_amount_retention', ctx=Store()),
                                                            op=Add(),
                                                            value=Subscript(
                                                                value=Name(id='tax_values', ctx=Load()),
                                                                slice=Constant(value='tax_amount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='tax_values', ctx=Load()),
                                                                    slice=Constant(value='l10n_es_type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='no_sujeto', kind=None)],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='base_amount_not_subject', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Subscript(
                                                                        value=Name(id='tax_values', ctx=Load()),
                                                                        slice=Constant(value='base_amount', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='tax_values', ctx=Load()),
                                                                            slice=Constant(value='l10n_es_type', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='no_sujeto_loc', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Name(id='base_amount_not_subject_loc', ctx=Store()),
                                                                            op=Add(),
                                                                            value=Subscript(
                                                                                value=Name(id='tax_values', ctx=Load()),
                                                                                slice=Constant(value='base_amount', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Subscript(
                                                                                    value=Name(id='tax_values', ctx=Load()),
                                                                                    slice=Constant(value='l10n_es_type', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='ignore', kind=None)],
                                                                            ),
                                                                            body=[Continue()],
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
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='tax_values', ctx=Load()),
                                                    slice=Constant(value='l10n_es_type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='retencion', kind=None),
                                                            Constant(value='recargo', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='base_amount', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='sign', ctx=Load()),
                                                        op=Mult(),
                                                        right=Subscript(
                                                            value=Name(id='tax_values', ctx=Load()),
                                                            slice=Constant(value='base_amount', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tax_details_info', ctx=Load()),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='DetalleIVA', kind=None),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='tax_info', ctx=Store())],
                                                    value=Dict(
                                                        keys=[Constant(value='BaseImponible', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Name(id='round', ctx=Load()),
                                                                args=[
                                                                    Name(id='base_amount', ctx=Load()),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='tax_values', ctx=Load()),
                                                            slice=Constant(value='applied_tax_amount', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0.0, kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='tax_info', ctx=Load()),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Subscript(
                                                                                value=Name(id='tax_values', ctx=Load()),
                                                                                slice=Constant(value='applied_tax_amount', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Name(id='round', ctx=Load()),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='math', ctx=Load()),
                                                                                            attr='copysign',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Subscript(
                                                                                                value=Name(id='tax_values', ctx=Load()),
                                                                                                slice=Constant(value='tax_amount', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Name(id='base_amount', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    Constant(value=2, kind=None),
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
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='tax_values', ctx=Load()),
                                                        slice=Constant(value='l10n_es_bien_inversion', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='tax_info', ctx=Load()),
                                                                    slice=Constant(value='BienInversion', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='S', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='recargo', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='recargo_tax_details', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tax_values', ctx=Load()),
                                                                        slice=Constant(value='group_tax_details', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='tax_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='recargo', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='tax_info', ctx=Load()),
                                                                    slice=Constant(value='CuotaRecargoEquivalencia', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Name(id='round', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='sign', ctx=Load()),
                                                                        op=Mult(),
                                                                        right=Subscript(
                                                                            value=Name(id='recargo', ctx=Load()),
                                                                            slice=Constant(value='tax_amount', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='tax_info', ctx=Load()),
                                                                    slice=Constant(value='TipoRecargoEquivalencia', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='recargo', ctx=Load()),
                                                                slice=Constant(value='applied_tax_amount', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='tax_details_info', ctx=Load()),
                                                                slice=Constant(value='DetalleIVA', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tax_info', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                attr='is_zero',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='base_amount_not_subject', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='tax_details_info', ctx=Load()),
                                                slice=Constant(value='NoSujeta', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='ImportePorArticulos7_14_Otros', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='sign', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='base_amount_not_subject', ctx=Load()),
                                            ),
                                            Constant(value=2, kind=None),
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
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='invoice', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                                attr='is_zero',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='base_amount_not_subject_loc', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='tax_details_info', ctx=Load()),
                                                slice=Constant(value='NoSujeta', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='ImporteTAIReglasLocalizacion', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='sign', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='base_amount_not_subject_loc', ctx=Load()),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
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
                                    Constant(value='tax_details_info', kind=None),
                                    Constant(value='tax_details', kind=None),
                                    Constant(value='tax_amount_deductible', kind=None),
                                    Constant(value='tax_amount_retention', kind=None),
                                    Constant(value='base_amount_not_subject', kind=None),
                                ],
                                values=[
                                    Name(id='tax_details_info', ctx=Load()),
                                    Name(id='tax_details', ctx=Load()),
                                    Name(id='tax_amount_deductible', ctx=Load()),
                                    Name(id='tax_amount_retention', ctx=Load()),
                                    Name(id='base_amount_not_subject', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_l10n_es_edi_get_partner_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='eu_country_codes', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
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
                                                    keywords=[],
                                                ),
                                                attr='country_ids',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='code', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_info', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IDOtro_ID', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                    Constant(value='NO_DISPONIBLE', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='ES', kind=None)],
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='partner_info', ctx=Load()),
                                            slice=Constant(value='NIF', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='vat',
                                                    ctx=Load(),
                                                ),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='ES', kind=None)],
                                            keywords=[],
                                        ),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=Constant(value=2, kind=None),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        orelse=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='vat',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            attr='code',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='eu_country_codes', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='partner_info', ctx=Load()),
                                                    slice=Constant(value='IDOtro', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='IDType', kind=None),
                                                    Constant(value='ID', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='02', kind=None),
                                                    Name(id='IDOtro_ID', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='partner_info', ctx=Load()),
                                                    slice=Constant(value='IDOtro', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[Constant(value='ID', kind=None)],
                                                values=[Name(id='IDOtro_ID', ctx=Load())],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='vat',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='partner_info', ctx=Load()),
                                                                slice=Constant(value='IDOtro', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='IDType', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='04', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='partner_info', ctx=Load()),
                                                                slice=Constant(value='IDOtro', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='IDType', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='06', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='partner_info', ctx=Load()),
                                                                slice=Constant(value='IDOtro', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='CodigoPais', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
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
                        Return(
                            value=Name(id='partner_info', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_l10n_es_edi_get_invoices_info',
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
                        Assign(
                            targets=[Name(id='eu_country_codes', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
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
                                                    keywords=[],
                                                ),
                                                attr='country_ids',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='code', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='simplified_partner', ctx=Store())],
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
                                args=[Constant(value='l10n_es_edi_sii.partner_simplified', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='info_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='invoice', ctx=Store()),
                            iter=Name(id='invoices', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='com_partner', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='commercial_partner_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_simplified', ctx=Store())],
                                    value=Compare(
                                        left=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='simplified_partner', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='info', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='PeriodoLiquidacion', kind=None),
                                            Constant(value='IDFactura', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='Ejercicio', kind=None),
                                                    Constant(value='Periodo', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='invoice', ctx=Load()),
                                                                    attr='date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='year',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='invoice', ctx=Load()),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='month',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='zfill',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=2, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='FechaExpedicionFacturaEmisor', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='invoice_date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%d-%m-%Y', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='invoice_node', ctx=Store()),
                                                Subscript(
                                                    value=Name(id='info', ctx=Load()),
                                                    slice=Constant(value='FacturaExpedida', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='invoice_node', ctx=Store()),
                                                Subscript(
                                                    value=Name(id='info', ctx=Load()),
                                                    slice=Constant(value='FacturaRecibida', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='partner_info', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_l10n_es_edi_get_partner_info',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='com_partner', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='invoice_node', ctx=Load()),
                                            slice=Constant(value='DescripcionOperacion', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='invoice_origin',
                                                ctx=Load(),
                                            ),
                                            Constant(value='manual', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='info', ctx=Load()),
                                                        slice=Constant(value='IDFactura', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='IDEmisorFactura', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[Constant(value='NIF', kind=None)],
                                                values=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='vat',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Slice(
                                                            lower=Constant(value=2, kind=None),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='info', ctx=Load()),
                                                        slice=Constant(value='IDFactura', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='NumSerieFacturaEmisor', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=60, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='is_simplified', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='Contraparte', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            None,
                                                            Constant(value='NombreRazon', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='partner_info', ctx=Load()),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='com_partner', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=120, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                                        operand=Attribute(
                                                            value=Name(id='com_partner', ctx=Load()),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='com_partner', ctx=Load()),
                                                                attr='country_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='eu_country_codes', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='01', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='02', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='info', ctx=Load()),
                                                        slice=Constant(value='IDFactura', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='IDEmisorFactura', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='partner_info', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='info', ctx=Load()),
                                                        slice=Constant(value='IDFactura', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='NumSerieFacturaEmisor', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=60, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='is_simplified', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='Contraparte', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            None,
                                                            Constant(value='NombreRazon', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='partner_info', ctx=Load()),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='com_partner', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=120, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='l10n_es_registration_date',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='FechaRegContable', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='invoice', ctx=Load()),
                                                                attr='l10n_es_registration_date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%d-%m-%Y', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='FechaRegContable', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='fields', ctx=Load()),
                                                                        attr='Date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='context_today',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='self', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='%d-%m-%Y', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='com_partner', ctx=Load()),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='com_partner', ctx=Load()),
                                                                attr='country_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='ES', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='01', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='09', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='move_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='out_invoice', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='invoice_node', ctx=Load()),
                                                    slice=Constant(value='TipoFactura', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Name(id='is_simplified', ctx=Load()),
                                                body=Constant(value='F2', kind=None),
                                                orelse=Constant(value='F1', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='invoice', ctx=Load()),
                                                    attr='move_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='out_refund', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='TipoFactura', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=IfExp(
                                                        test=Name(id='is_simplified', ctx=Load()),
                                                        body=Constant(value='R5', kind=None),
                                                        orelse=Constant(value='R1', kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='TipoRectificativa', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='I', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='invoice', ctx=Load()),
                                                            attr='move_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='in_invoice', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='invoice_node', ctx=Load()),
                                                                    slice=Constant(value='TipoFactura', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='F1', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='invoice', ctx=Load()),
                                                                    attr='move_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='in_refund', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='invoice_node', ctx=Load()),
                                                                            slice=Constant(value='TipoFactura', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='R4', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='invoice_node', ctx=Load()),
                                                                            slice=Constant(value='TipoRectificativa', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='I', kind=None),
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
                                Assign(
                                    targets=[Name(id='sign', ctx=Store())],
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='is_sale_document',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        body=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        orelse=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='invoice', ctx=Load()),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='com_partner', ctx=Load()),
                                                                attr='country_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='ES', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='com_partner', ctx=Load()),
                                                                            attr='vat',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value='', kind=None),
                                                                    ],
                                                                ),
                                                                attr='startswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='ESN', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tax_details_info_vals', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_l10n_es_edi_get_invoices_tax_details_info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='invoice', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='TipoDesglose', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[Constant(value='DesgloseFactura', kind=None)],
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='tax_details_info_vals', ctx=Load()),
                                                                slice=Constant(value='tax_details_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='ImporteTotal', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='round', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='sign', ctx=Load()),
                                                                op=Mult(),
                                                                right=BinOp(
                                                                    left=BinOp(
                                                                        left=Subscript(
                                                                            value=Subscript(
                                                                                value=Name(id='tax_details_info_vals', ctx=Load()),
                                                                                slice=Constant(value='tax_details', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='base_amount', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Subscript(
                                                                            value=Subscript(
                                                                                value=Name(id='tax_details_info_vals', ctx=Load()),
                                                                                slice=Constant(value='tax_details', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='tax_amount', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    op=Sub(),
                                                                    right=Subscript(
                                                                        value=Name(id='tax_details_info_vals', ctx=Load()),
                                                                        slice=Constant(value='tax_amount_retention', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='tax_details_info_service_vals', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_l10n_es_edi_get_invoices_tax_details_info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='invoice', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='filter_invl_to_apply',
                                                                value=Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Call(
                                                                        func=Name(id='any', ctx=Load()),
                                                                        args=[
                                                                            GeneratorExp(
                                                                                elt=Compare(
                                                                                    left=Attribute(
                                                                                        value=Name(id='t', ctx=Load()),
                                                                                        attr='tax_scope',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Constant(value='service', kind=None)],
                                                                                ),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Name(id='t', ctx=Store()),
                                                                                        iter=Attribute(
                                                                                            value=Name(id='x', ctx=Load()),
                                                                                            attr='tax_ids',
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
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='tax_details_info_consu_vals', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_l10n_es_edi_get_invoices_tax_details_info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='invoice', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='filter_invl_to_apply',
                                                                value=Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='x', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Call(
                                                                        func=Name(id='any', ctx=Load()),
                                                                        args=[
                                                                            GeneratorExp(
                                                                                elt=Compare(
                                                                                    left=Attribute(
                                                                                        value=Name(id='t', ctx=Load()),
                                                                                        attr='tax_scope',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Constant(value='consu', kind=None)],
                                                                                ),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Name(id='t', ctx=Store()),
                                                                                        iter=Attribute(
                                                                                            value=Name(id='x', ctx=Load()),
                                                                                            attr='tax_ids',
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
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='tax_details_info_service_vals', ctx=Load()),
                                                        slice=Constant(value='tax_details_info', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='invoice_node', ctx=Load()),
                                                                    attr='setdefault',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='TipoDesglose', kind=None),
                                                                    Dict(keys=[], values=[]),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='invoice_node', ctx=Load()),
                                                                        slice=Constant(value='TipoDesglose', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='setdefault',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='DesgloseTipoOperacion', kind=None),
                                                                    Dict(keys=[], values=[]),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='invoice_node', ctx=Load()),
                                                                            slice=Constant(value='TipoDesglose', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='DesgloseTipoOperacion', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='PrestacionServicios', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='tax_details_info_service_vals', ctx=Load()),
                                                                slice=Constant(value='tax_details_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='tax_details_info_consu_vals', ctx=Load()),
                                                        slice=Constant(value='tax_details_info', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='invoice_node', ctx=Load()),
                                                                    attr='setdefault',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='TipoDesglose', kind=None),
                                                                    Dict(keys=[], values=[]),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='invoice_node', ctx=Load()),
                                                                        slice=Constant(value='TipoDesglose', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='setdefault',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='DesgloseTipoOperacion', kind=None),
                                                                    Dict(keys=[], values=[]),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='invoice_node', ctx=Load()),
                                                                            slice=Constant(value='TipoDesglose', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='DesgloseTipoOperacion', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='Entrega', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='tax_details_info_consu_vals', ctx=Load()),
                                                                slice=Constant(value='tax_details_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='invoice_node', ctx=Load()),
                                                            slice=Constant(value='ImporteTotal', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='round', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='sign', ctx=Load()),
                                                                op=Mult(),
                                                                right=BinOp(
                                                                    left=BinOp(
                                                                        left=BinOp(
                                                                            left=BinOp(
                                                                                left=BinOp(
                                                                                    left=Subscript(
                                                                                        value=Subscript(
                                                                                            value=Name(id='tax_details_info_service_vals', ctx=Load()),
                                                                                            slice=Constant(value='tax_details', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='base_amount', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    op=Add(),
                                                                                    right=Subscript(
                                                                                        value=Subscript(
                                                                                            value=Name(id='tax_details_info_service_vals', ctx=Load()),
                                                                                            slice=Constant(value='tax_details', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='tax_amount', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                                op=Sub(),
                                                                                right=Subscript(
                                                                                    value=Name(id='tax_details_info_service_vals', ctx=Load()),
                                                                                    slice=Constant(value='tax_amount_retention', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            op=Add(),
                                                                            right=Subscript(
                                                                                value=Subscript(
                                                                                    value=Name(id='tax_details_info_consu_vals', ctx=Load()),
                                                                                    slice=Constant(value='tax_details', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='base_amount', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Subscript(
                                                                            value=Subscript(
                                                                                value=Name(id='tax_details_info_consu_vals', ctx=Load()),
                                                                                slice=Constant(value='tax_details', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value='tax_amount', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    op=Sub(),
                                                                    right=Subscript(
                                                                        value=Name(id='tax_details_info_consu_vals', ctx=Load()),
                                                                        slice=Constant(value='tax_amount_retention', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='tax_details_info_isp_vals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_l10n_es_edi_get_invoices_tax_details_info',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='invoice', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='filter_invl_to_apply',
                                                        value=Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=Call(
                                                                func=Name(id='any', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=Name(id='t', ctx=Load()),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='t', ctx=Store()),
                                                                                iter=Attribute(
                                                                                    value=Name(id='x', ctx=Load()),
                                                                                    attr='tax_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ifs=[
                                                                                    Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='t', ctx=Load()),
                                                                                            attr='l10n_es_type',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='sujeto_isp', kind=None)],
                                                                                    ),
                                                                                ],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='tax_details_info_other_vals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_l10n_es_edi_get_invoices_tax_details_info',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='invoice', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='filter_invl_to_apply',
                                                        value=Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Name(id='any', ctx=Load()),
                                                                    args=[
                                                                        GeneratorExp(
                                                                            elt=Name(id='t', ctx=Load()),
                                                                            generators=[
                                                                                comprehension(
                                                                                    target=Name(id='t', ctx=Store()),
                                                                                    iter=Attribute(
                                                                                        value=Name(id='x', ctx=Load()),
                                                                                        attr='tax_ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ifs=[
                                                                                        Compare(
                                                                                            left=Attribute(
                                                                                                value=Name(id='t', ctx=Load()),
                                                                                                attr='l10n_es_type',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            ops=[Eq()],
                                                                                            comparators=[Constant(value='sujeto_isp', kind=None)],
                                                                                        ),
                                                                                    ],
                                                                                    is_async=0,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='invoice_node', ctx=Load()),
                                                    slice=Constant(value='DesgloseFactura', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Subscript(
                                                value=Name(id='tax_details_info_isp_vals', ctx=Load()),
                                                slice=Constant(value='tax_details_info', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='invoice_node', ctx=Load()),
                                                                slice=Constant(value='DesgloseFactura', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='InversionSujetoPasivo', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='tax_details_info_isp_vals', ctx=Load()),
                                                        slice=Constant(value='tax_details_info', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Subscript(
                                                value=Name(id='tax_details_info_other_vals', ctx=Load()),
                                                slice=Constant(value='tax_details_info', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='invoice_node', ctx=Load()),
                                                                slice=Constant(value='DesgloseFactura', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='DesgloseIVA', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='tax_details_info_other_vals', ctx=Load()),
                                                        slice=Constant(value='tax_details_info', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='invoice_node', ctx=Load()),
                                                    slice=Constant(value='ImporteTotal', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='round', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='sign', ctx=Load()),
                                                        op=Mult(),
                                                        right=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=BinOp(
                                                                            left=Subscript(
                                                                                value=Subscript(
                                                                                    value=Name(id='tax_details_info_isp_vals', ctx=Load()),
                                                                                    slice=Constant(value='tax_details', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='base_amount', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            op=Add(),
                                                                            right=Subscript(
                                                                                value=Subscript(
                                                                                    value=Name(id='tax_details_info_isp_vals', ctx=Load()),
                                                                                    slice=Constant(value='tax_details', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='tax_amount', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                        op=Sub(),
                                                                        right=Subscript(
                                                                            value=Name(id='tax_details_info_isp_vals', ctx=Load()),
                                                                            slice=Constant(value='tax_amount_retention', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='tax_details_info_other_vals', ctx=Load()),
                                                                            slice=Constant(value='tax_details', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='base_amount', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='tax_details_info_other_vals', ctx=Load()),
                                                                        slice=Constant(value='tax_details', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='tax_amount', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            op=Sub(),
                                                            right=Subscript(
                                                                value=Name(id='tax_details_info_other_vals', ctx=Load()),
                                                                slice=Constant(value='tax_amount_retention', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='invoice_node', ctx=Load()),
                                                    slice=Constant(value='CuotaDeducible', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='round', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='sign', ctx=Load()),
                                                        op=Mult(),
                                                        right=BinOp(
                                                            left=Subscript(
                                                                value=Name(id='tax_details_info_isp_vals', ctx=Load()),
                                                                slice=Constant(value='tax_amount_deductible', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Subscript(
                                                                value=Name(id='tax_details_info_other_vals', ctx=Load()),
                                                                slice=Constant(value='tax_amount_deductible', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='info_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='info', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='info_list', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_l10n_es_edi_web_service_aeat_vals',
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
                            test=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='invoices', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='is_sale_document',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='url', kind=None)],
                                        values=[Constant(value='https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/aplicaciones/es/aeat/ssii_1_1/fact/ws/SuministroFactEmitidas.wsdl', kind=None)],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='url', kind=None)],
                                        values=[Constant(value='https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/aplicaciones/es/aeat/ssii_1_1/fact/ws/SuministroFactRecibidas.wsdl', kind=None)],
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
                    name='_l10n_es_edi_web_service_bizkaia_vals',
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
                            test=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='invoices', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='is_sale_document',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='url', kind=None),
                                            Constant(value='test_url', kind=None),
                                        ],
                                        values=[
                                            Constant(value='https://www.bizkaia.eus/ogasuna/sii/documentos/SuministroFactEmitidas.wsdl', kind=None),
                                            Constant(value='https://pruapps.bizkaia.eus/SSII-FACT/ws/fe/SiiFactFEV1SOAP', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='url', kind=None),
                                            Constant(value='test_url', kind=None),
                                        ],
                                        values=[
                                            Constant(value='https://www.bizkaia.eus/ogasuna/sii/documentos/SuministroFactRecibidas.wsdl', kind=None),
                                            Constant(value='https://pruapps.bizkaia.eus/SSII-FACT/ws/fr/SiiFactFRV1SOAP', kind=None),
                                        ],
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
                    name='_l10n_es_edi_web_service_gipuzkoa_vals',
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
                            test=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='invoices', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='is_sale_document',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='url', kind=None),
                                            Constant(value='test_url', kind=None),
                                        ],
                                        values=[
                                            Constant(value='https://egoitza.gipuzkoa.eus/ogasuna/sii/ficheros/v1.1/SuministroFactEmitidas.wsdl', kind=None),
                                            Constant(value='https://sii-prep.egoitza.gipuzkoa.eus/JBS/HACI/SSII-FACT/ws/fe/SiiFactFEV1SOAP', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='url', kind=None),
                                            Constant(value='test_url', kind=None),
                                        ],
                                        values=[
                                            Constant(value='https://egoitza.gipuzkoa.eus/ogasuna/sii/ficheros/v1.1/SuministroFactRecibidas.wsdl', kind=None),
                                            Constant(value='https://sii-prep.egoitza.gipuzkoa.eus/JBS/HACI/SSII-FACT/ws/fr/SiiFactFRV1SOAP', kind=None),
                                        ],
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
                    name='_l10n_es_edi_call_web_service_sign',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoices', annotation=None, type_comment=None),
                            arg(arg='info_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
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
                            targets=[Name(id='csv_number', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='invoices', ctx=Load()),
                                        attr='mapped',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='l10n_es_edi_csv', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoices', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='inv', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='inv', ctx=Load()),
                                                        attr='l10n_es_registration_date',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='l10n_es_registration_date', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context_today',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='self', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='l10n_es_edi_tax_agency', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='mapped',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='l10n_es_edi_tax_agency', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='connection_vals', ctx=Store())],
                            value=Call(
                                func=Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='self', ctx=Load()),
                                        JoinedStr(
                                            values=[
                                                Constant(value='_l10n_es_edi_web_service_', kind=None),
                                                FormattedValue(
                                                    value=Name(id='l10n_es_edi_tax_agency', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value='_vals', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                args=[Name(id='invoices', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='header', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='IDVersionSii', kind=None),
                                    Constant(value='Titular', kind=None),
                                    Constant(value='TipoComunicacion', kind=None),
                                ],
                                values=[
                                    Constant(value='1.1', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='NombreRazon', kind=None),
                                            Constant(value='NIF', kind=None),
                                        ],
                                        values=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=120, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='company', ctx=Load()),
                                                    attr='vat',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=2, kind=None),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    IfExp(
                                        test=Name(id='csv_number', ctx=Load()),
                                        body=Constant(value='A1', kind=None),
                                        orelse=Constant(value='A0', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='session', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='Session',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='session', ctx=Load()),
                                    attr='cert',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='company', ctx=Load()),
                                attr='l10n_es_edi_certificate_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='session', ctx=Load()),
                                    attr='mount',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='https://', kind=None),
                                    Call(
                                        func=Name(id='PatchedHTTPAdapter', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='transport', ctx=Store())],
                            value=Call(
                                func=Name(id='Transport', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='operation_timeout',
                                        value=Constant(value=60, kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=60, kind=None),
                                    ),
                                    keyword(
                                        arg='session',
                                        value=Name(id='session', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='client', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='zeep', ctx=Load()),
                                    attr='Client',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='connection_vals', ctx=Load()),
                                        slice=Constant(value='url', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='transport',
                                        value=Name(id='transport', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='invoices', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='is_sale_document',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='service_name', ctx=Store())],
                                    value=Constant(value='SuministroFactEmitidas', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='service_name', ctx=Store())],
                                    value=Constant(value='SuministroFactRecibidas', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='l10n_es_edi_test_env',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='connection_vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='test_url', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='service_name', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='Pruebas', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='serv', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='client', ctx=Load()),
                                    attr='bind',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='siiService', kind=None),
                                    Name(id='service_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='l10n_es_edi_test_env',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='connection_vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_url', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='serv', ctx=Load()),
                                                attr='_binding_options',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='address', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='connection_vals', ctx=Load()),
                                        slice=Constant(value='test_url', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='invoices', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='serv', ctx=Load()),
                                                    attr='SuministroLRFacturasEmitidas',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='header', ctx=Load()),
                                                    Name(id='info_list', ctx=Load()),
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
                                                    value=Name(id='serv', ctx=Load()),
                                                    attr='SuministroLRFacturasRecibidas',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='header', ctx=Load()),
                                                    Name(id='info_list', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='SSLError',
                                        ctx=Load(),
                                    ),
                                    name='error',
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The SSL certificate could not be validated.', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='zeep', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='Error',
                                        ctx=Load(),
                                    ),
                                    name='error',
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Networking error:\n%s', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Name(id='error', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='error',
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='error', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[
                                If(
                                    test=Name(id='msg', ctx=Load()),
                                    body=[
                                        Return(
                                            value=DictComp(
                                                key=Name(id='inv', ctx=Load()),
                                                value=Dict(
                                                    keys=[
                                                        Constant(value='error', kind=None),
                                                        Constant(value='blocking_level', kind=None),
                                                    ],
                                                    values=[
                                                        Name(id='msg', ctx=Load()),
                                                        Constant(value='warning', kind=None),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='inv', ctx=Store()),
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
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='res', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='RespuestaLinea',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=DictComp(
                                        key=Name(id='inv', ctx=Load()),
                                        value=Dict(
                                            keys=[
                                                Constant(value='error', kind=None),
                                                Constant(value='blocking_level', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='The web service is not responding', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='warning', kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='inv', ctx=Store()),
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
                        Assign(
                            targets=[Name(id='resp_state', ctx=Store())],
                            value=Subscript(
                                value=Name(id='res', ctx=Load()),
                                slice=Constant(value='EstadoEnvio', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='l10n_es_edi_csv', ctx=Store())],
                            value=Subscript(
                                value=Name(id='res', ctx=Load()),
                                slice=Constant(value='CSV', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='resp_state', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='Correcto', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='invoices', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='l10n_es_edi_csv', kind=None)],
                                                values=[Name(id='l10n_es_edi_csv', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=DictComp(
                                        key=Name(id='inv', ctx=Load()),
                                        value=Dict(
                                            keys=[Constant(value='success', kind=None)],
                                            values=[Constant(value=True, kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='inv', ctx=Store()),
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
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='respl', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='res', ctx=Load()),
                                attr='RespuestaLinea',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='invoice_number', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='respl', ctx=Load()),
                                            attr='IDFactura',
                                            ctx=Load(),
                                        ),
                                        attr='NumSerieFacturaEmisor',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='invoices', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='is_sale_document',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='inv', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoices', ctx=Load()),
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
                                                        body=Compare(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=60, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='invoice_number', ctx=Load())],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='candidates', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='invoices', ctx=Load()),
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
                                                        body=Compare(
                                                            left=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='ref',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=60, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='invoice_number', ctx=Load())],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='candidates', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[GtE()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='respl_partner_info', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='respl', ctx=Load()),
                                                            attr='IDFactura',
                                                            ctx=Load(),
                                                        ),
                                                        attr='IDEmisorFactura',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='inv', ctx=Store())],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='candidate', ctx=Store()),
                                                    iter=Name(id='candidates', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='partner_info', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_l10n_es_edi_get_partner_info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='candidate', ctx=Load()),
                                                                        attr='commercial_partner_id',
                                                                        ctx=Load(),
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
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='partner_info', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='NIF', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='partner_info', ctx=Load()),
                                                                            slice=Constant(value='NIF', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='respl_partner_info', ctx=Load()),
                                                                                attr='NIF',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='inv', ctx=Store())],
                                                                    value=Name(id='candidate', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Break(),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='partner_info', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='IDOtro', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='all', ctx=Load()),
                                                                        args=[
                                                                            GeneratorExp(
                                                                                elt=Compare(
                                                                                    left=Call(
                                                                                        func=Name(id='getattr', ctx=Load()),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='respl_partner_info', ctx=Load()),
                                                                                                attr='IDOtro',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Name(id='k', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Name(id='v', ctx=Load())],
                                                                                ),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Tuple(
                                                                                            elts=[
                                                                                                Name(id='k', ctx=Store()),
                                                                                                Name(id='v', ctx=Store()),
                                                                                            ],
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                        iter=Call(
                                                                                            func=Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Name(id='partner_info', ctx=Load()),
                                                                                                    slice=Constant(value='IDOtro', kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='items',
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
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='inv', ctx=Store())],
                                                                    value=Name(id='candidate', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Break(),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='inv', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='inv', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='candidates', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='inv', ctx=Store())],
                                                    value=Name(id='candidates', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='resp_line_state', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='respl', ctx=Load()),
                                        attr='EstadoRegistro',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='resp_line_state', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='Correcto', kind=None),
                                                    Constant(value='AceptadoConErrores', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='inv', ctx=Load()),
                                                    attr='l10n_es_edi_csv',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='l10n_es_edi_csv', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='results', ctx=Load()),
                                                    slice=Name(id='inv', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[Constant(value='success', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='resp_line_state', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='AceptadoConErrores', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='inv', ctx=Load()),
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
                                                                        args=[Constant(value='This was accepted with errors: ', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Add(),
                                                                    right=Call(
                                                                        func=Name(id='html_escape', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='respl', ctx=Load()),
                                                                                attr='DescripcionErrorRegistro',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='respl', ctx=Load()),
                                                attr='RegistroDuplicado',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='results', ctx=Load()),
                                                            slice=Name(id='inv', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[Constant(value='success', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='inv', ctx=Load()),
                                                            attr='message_post',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='We saw that this invoice was sent correctly before, but we did not treat the response.  Make sure it is not because of a wrong configuration.', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='results', ctx=Load()),
                                                            slice=Name(id='inv', ctx=Load()),
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
                                                                args=[
                                                                    Constant(value='[%s] %s', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='respl', ctx=Load()),
                                                                        attr='CodigoErrorRegistro',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='respl', ctx=Load()),
                                                                        attr='DescripcionErrorRegistro',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                    name='_is_required_for_invoice',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='es_sii', kind=None)],
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
                                            attr='_is_required_for_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoice', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='invoice', ctx=Load()),
                                attr='l10n_es_edi_is_required',
                                ctx=Load(),
                            ),
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
                                        comparators=[Constant(value='es_sii', kind=None)],
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
                                ops=[NotEq()],
                                comparators=[Constant(value='es_sii', kind=None)],
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
                            orelse=[],
                        ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_batch_key',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move', annotation=None, type_comment=None),
                            arg(arg='state', annotation=None, type_comment=None),
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
                                comparators=[Constant(value='es_sii', kind=None)],
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
                                            attr='_get_batch_key',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='move', ctx=Load()),
                                            Name(id='state', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='move_type',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='l10n_es_edi_csv',
                                        ctx=Load(),
                                    ),
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
                                comparators=[Constant(value='es_sii', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='vat',
                                    ctx=Load(),
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
                                                args=[
                                                    Constant(value='VAT number is missing on company %s', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
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
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='vat',
                                    ctx=Load(),
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
                                                args=[
                                                    Constant(value='VAT number needs to be configured on the partner %s', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
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
                            orelse=[],
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='invoice_line_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='display_type',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='taxes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='tax_ids',
                                                ctx=Load(),
                                            ),
                                            attr='flatten_taxes_hierarchy',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='recargo_count', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='taxes', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='l10n_es_type', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='count',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='recargo', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='retention_count', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='taxes', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='l10n_es_type', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='count',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='retencion', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sujeto_count', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='taxes', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='l10n_es_type', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='count',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='sujeto', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='no_sujeto_count', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='taxes', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='l10n_es_type', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='count',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='no_sujeto', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='no_sujeto_loc_count', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='taxes', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='l10n_es_type', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='count',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='no_sujeto_loc', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='retention_count', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
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
                                                        args=[
                                                            Constant(value='Line %s should only have one retention tax.', kind=None),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='display_name',
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
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='recargo_count', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
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
                                                        args=[
                                                            Constant(value='Line %s should only have one recargo tax.', kind=None),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='display_name',
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
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='sujeto_count', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
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
                                                        args=[
                                                            Constant(value='Line %s should only have one sujeto tax.', kind=None),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='display_name',
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
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='no_sujeto_count', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
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
                                                        args=[
                                                            Constant(value='Line %s should only have one no sujeto tax.', kind=None),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='display_name',
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
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='no_sujeto_loc_count', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
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
                                                        args=[
                                                            Constant(value='Line %s should only have one no sujeto (localizations) tax.', kind=None),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='display_name',
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
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Name(id='sujeto_count', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='no_sujeto_loc_count', ctx=Load()),
                                            ),
                                            op=Add(),
                                            right=Name(id='no_sujeto_count', ctx=Load()),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
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
                                                        args=[
                                                            Constant(value='Line %s should only have one main tax.', kind=None),
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='display_name',
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
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='move', ctx=Load()),
                                    attr='move_type',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='in_invoice', kind=None),
                                            Constant(value='in_refund', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='ref',
                                            ctx=Load(),
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
                                                        args=[Constant(value='You should put a vendor reference on this vendor bill. ', kind=None)],
                                                        keywords=[],
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
                    name='_is_compatible_with_journal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='journal', annotation=None, type_comment=None),
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
                                comparators=[Constant(value='es_sii', kind=None)],
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
                                            attr='_is_compatible_with_journal',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='journal', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='journal', ctx=Load()),
                                    attr='country_code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='ES', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_invoice_edi',
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
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='es_sii', kind=None)],
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
                                            attr='_post_invoice_edi',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='invoices', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='certificate', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='invoices', ctx=Load()),
                                    attr='company_id',
                                    ctx=Load(),
                                ),
                                attr='l10n_es_edi_certificate_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='certificate', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=DictComp(
                                        key=Name(id='inv', ctx=Load()),
                                        value=Dict(
                                            keys=[
                                                Constant(value='error', kind=None),
                                                Constant(value='blocking_level', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Please configure the certificate for SII.', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='error', kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='inv', ctx=Store()),
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
                        Assign(
                            targets=[Name(id='l10n_es_edi_tax_agency', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='invoices', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='mapped',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='l10n_es_edi_tax_agency', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='l10n_es_edi_tax_agency', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=DictComp(
                                        key=Name(id='inv', ctx=Load()),
                                        value=Dict(
                                            keys=[
                                                Constant(value='error', kind=None),
                                                Constant(value='blocking_level', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Please specify a tax agency on your company for SII.', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='error', kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='inv', ctx=Store()),
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
                        Assign(
                            targets=[Name(id='info_list', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_l10n_es_edi_get_invoices_info',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoices', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_l10n_es_edi_call_web_service_sign',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoices', ctx=Load()),
                                    Name(id='info_list', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='inv', ctx=Store()),
                            iter=Name(id='invoices', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='inv', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='success', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
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
                                                            Constant(value='type', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='raw', kind=None),
                                                            Constant(value='mimetype', kind=None),
                                                            Constant(value='res_model', kind=None),
                                                            Constant(value='res_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='binary', kind=None),
                                                            Constant(value='jsondump.json', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='json', ctx=Load()),
                                                                    attr='dumps',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='info_list', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='application/json', kind=None),
                                                            Attribute(
                                                                value=Name(id='inv', ctx=Load()),
                                                                attr='_name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='inv', ctx=Load()),
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
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Name(id='inv', ctx=Load()),
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
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
