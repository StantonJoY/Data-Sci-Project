Module(
    body=[
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_module_resource', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest',
            names=[alias(name='mock', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        FunctionDef(
            name='_generate_mocked_needs_web_services',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='needs_web_services', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='edi_format', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Name(id='needs_web_services', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_generate_mocked_support_batching',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='support_batching', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[
                                arg(arg='edi_format', annotation=None, type_comment=None),
                                arg(arg='move', annotation=None, type_comment=None),
                                arg(arg='state', annotation=None, type_comment=None),
                                arg(arg='company', annotation=None, type_comment=None),
                            ],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Name(id='support_batching', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_mocked_get_batch_key',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='edi_format', annotation=None, type_comment=None),
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
                Return(
                    value=Tuple(elts=[], ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_mocked_check_move_configuration_success',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='edi_format', annotation=None, type_comment=None),
                    arg(arg='move', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=List(elts=[], ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_mocked_check_move_configuration_fail',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='edi_format', annotation=None, type_comment=None),
                    arg(arg='move', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=List(
                        elts=[Constant(value='Fake error (mocked)', kind=None)],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_mocked_post',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='edi_format', annotation=None, type_comment=None),
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
                    targets=[Name(id='res', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                For(
                    target=Name(id='invoice', ctx=Store()),
                    iter=Name(id='invoices', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='edi_format', ctx=Load()),
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
                                            Constant(value='mimetype', kind=None),
                                        ],
                                        values=[
                                            Constant(value='mock_simple.xml', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='encodebytes',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=b"<?xml version='1.0' encoding='UTF-8'?><Invoice/>", kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='application/xml', kind=None),
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
                                    slice=Name(id='invoice', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='success', kind=None),
                                    Constant(value='attachment', kind=None),
                                ],
                                values=[
                                    Constant(value=True, kind=None),
                                    Name(id='attachment', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
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
        FunctionDef(
            name='_mocked_post_two_steps',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='edi_format', annotation=None, type_comment=None),
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
                    targets=[Name(id='invoices_no_ref', ctx=Store())],
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
                                    args=[arg(arg='i', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=UnaryOp(
                                    op=Not(),
                                    operand=Attribute(
                                        value=Name(id='i', ctx=Load()),
                                        attr='ref',
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
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='invoices_no_ref', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[
                            Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='invoices', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='invoices_no_ref', ctx=Load()),
                                    attr='ref',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='test_ref', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Name(id='invoice', ctx=Load()),
                                value=Dict(keys=[], values=[]),
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
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='invoices_no_ref', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='invoice', ctx=Store()),
                                    iter=Name(id='invoices', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attachment', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='edi_format', ctx=Load()),
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
                                                            Constant(value='mimetype', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mock_simple.xml', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='base64', ctx=Load()),
                                                                    attr='encodebytes',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=b"<?xml version='1.0' encoding='UTF-8'?><Invoice/>", kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='application/xml', kind=None),
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
                                                    slice=Name(id='invoice', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='success', kind=None),
                                                    Constant(value='attachment', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Name(id='attachment', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[Constant(value='wrong use of "_mocked_post_two_steps"', kind=None)],
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
            name='_mocked_cancel_success',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='edi_format', annotation=None, type_comment=None),
                    arg(arg='invoices', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=DictComp(
                        key=Name(id='invoice', ctx=Load()),
                        value=Dict(
                            keys=[Constant(value='success', kind=None)],
                            values=[Constant(value=True, kind=None)],
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_mocked_cancel_failed',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='edi_format', annotation=None, type_comment=None),
                    arg(arg='invoices', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=DictComp(
                        key=Name(id='invoice', ctx=Load()),
                        value=Dict(
                            keys=[Constant(value='error', kind=None)],
                            values=[Constant(value='Faked error (mocked)', kind=None)],
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='AccountEdiTestCommon',
            bases=[Name(id='AccountTestInvoicingCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='chart_template_ref', annotation=None, type_comment=None),
                            arg(arg='edi_format_ref', annotation=None, type_comment=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='chart_template_ref',
                                        value=Name(id='chart_template_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=Name(id='edi_format_ref', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='edi_format',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='edi_format_ref', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='edi_format',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='account.edi.format', kind=None),
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
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='code', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Test EDI format', kind=None),
                                                    Constant(value='test_edi', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='journal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_journal_sale', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='journal',
                                        ctx=Load(),
                                    ),
                                    attr='edi_format_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='edi_format',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='mock_edi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='_is_required_for_invoice_method', annotation=None, type_comment=None),
                            arg(arg='_is_required_for_payment_method', annotation=None, type_comment=None),
                            arg(arg='_support_batching_method', annotation=None, type_comment=None),
                            arg(arg='_get_batch_key_method', annotation=None, type_comment=None),
                            arg(arg='_needs_web_services_method', annotation=None, type_comment=None),
                            arg(arg='_check_move_configuration_method', annotation=None, type_comment=None),
                            arg(arg='_post_invoice_edi_method', annotation=None, type_comment=None),
                            arg(arg='_cancel_invoice_edi_method', annotation=None, type_comment=None),
                            arg(arg='_post_payment_edi_method', annotation=None, type_comment=None),
                            arg(arg='_cancel_payment_edi_method', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[
                                        arg(arg='edi_format', annotation=None, type_comment=None),
                                        arg(arg='invoice', annotation=None, type_comment=None),
                                    ],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Constant(value=True, kind=None),
                            ),
                            Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[
                                        arg(arg='edi_format', annotation=None, type_comment=None),
                                        arg(arg='invoice', annotation=None, type_comment=None),
                                    ],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Constant(value=True, kind=None),
                            ),
                            Call(
                                func=Name(id='_generate_mocked_support_batching', ctx=Load()),
                                args=[Constant(value=False, kind=None)],
                                keywords=[],
                            ),
                            Name(id='_mocked_get_batch_key', ctx=Load()),
                            Call(
                                func=Name(id='_generate_mocked_needs_web_services', ctx=Load()),
                                args=[Constant(value=False, kind=None)],
                                keywords=[],
                            ),
                            Name(id='_mocked_check_move_configuration_success', ctx=Load()),
                            Name(id='_mocked_post', ctx=Load()),
                            Name(id='_mocked_cancel_success', ctx=Load()),
                            Name(id='_mocked_post', ctx=Load()),
                            Name(id='_mocked_cancel_success', ctx=Load()),
                        ],
                    ),
                    body=[
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._is_required_for_invoice', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_is_required_for_invoice_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._is_required_for_payment', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_is_required_for_payment_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._needs_web_services', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_needs_web_services_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._support_batching', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_support_batching_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._get_batch_key', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_get_batch_key_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._check_move_configuration', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_check_move_configuration_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._post_invoice_edi', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_post_invoice_edi_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._cancel_invoice_edi', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_cancel_invoice_edi_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._post_payment_edi', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_post_payment_edi_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.addons.account_edi.models.account_edi_format.AccountEdiFormat._cancel_payment_edi', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='new',
                                                        value=Name(id='_cancel_payment_edi_method', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Yield(value=None),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[Pass()],
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='edi_cron',
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
                                                        slice=Constant(value='account.edi.document', kind=None),
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
                                                            Constant(value='state', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='to_send', kind=None),
                                                                    Constant(value='to_cancel', kind=None),
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
                                    attr='_process_documents_web_services',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='with_commit',
                                        value=Constant(value=False, kind=None),
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
                    name='_create_empty_vendor_bill',
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
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='move_type', kind=None),
                                            Constant(value='journal_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='in_invoice', kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='default_journal_purchase', kind=None),
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
                        Return(
                            value=Name(id='invoice', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update_invoice_from_file',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module_name', annotation=None, type_comment=None),
                            arg(arg='subfolder', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='file_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_resource', ctx=Load()),
                                args=[
                                    Name(id='module_name', ctx=Load()),
                                    Name(id='subfolder', ctx=Load()),
                                    Name(id='filename', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='file', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='file_path', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                            Constant(value='res_id', kind=None),
                                            Constant(value='res_model', kind=None),
                                        ],
                                        values=[
                                            Name(id='filename', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='encodebytes',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='file', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='invoice', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='account.move', kind=None),
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
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='attachment_ids',
                                        value=List(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                    name='create_invoice_from_file',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module_name', annotation=None, type_comment=None),
                            arg(arg='subfolder', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='file_path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_resource', ctx=Load()),
                                args=[
                                    Name(id='module_name', ctx=Load()),
                                    Name(id='subfolder', ctx=Load()),
                                    Name(id='filename', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='file', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='file_path', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        ],
                                        values=[
                                            Name(id='filename', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='encodebytes',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='file', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='account.move', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='journal_id', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_journal_sale', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action_vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='journal_id', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_move_type',
                                                value=Constant(value='in_invoice', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create_invoice_from_attachment',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='attachment', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='action_vals', ctx=Load()),
                                        slice=Constant(value='res_id', kind=None),
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
                    name='assert_generated_file_equal',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='invoice', annotation=None, type_comment=None),
                            arg(arg='expected_values', annotation=None, type_comment=None),
                            arg(arg='applied_xpath', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='action_post',
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
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_process_documents_web_services',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='with_commit',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='_get_edi_attachment',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='edi_format',
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
                                operand=Name(id='attachment', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[Constant(value='No attachment was generated after posting EDI', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='xml_content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='bin_size',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='datas',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_etree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_xml_tree_from_string',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xml_content', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_etree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_xml_tree_from_string',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expected_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='applied_xpath', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='expected_etree', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_applied_xpath',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='expected_etree', ctx=Load()),
                                            Name(id='applied_xpath', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertXmlTreeEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='current_etree', ctx=Load()),
                                    Name(id='expected_etree', ctx=Load()),
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
                    name='create_edi_document',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='edi_format', annotation=None, type_comment=None),
                            arg(arg='state', annotation=None, type_comment=None),
                            arg(arg='move', annotation=None, type_comment=None),
                            arg(arg='move_type', annotation=None, type_comment=None),
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
                        Expr(
                            value=Constant(value=" Creates a document based on an existing invoice or creates one, too.\n\n        :param edi_format:  The edi_format of the document.\n        :param state:       The state of the document.\n        :param move:        The move of the document or None to create a new one.\n        :param move_type:   If move is None, the type of the invoice to create, defaults to 'out_invoice'.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='move', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='move', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='init_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='move_type', ctx=Load()),
                                                    Constant(value='out_invoice', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='products',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_a',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='account.edi.document', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='edi_format_id', kind=None),
                                            Constant(value='move_id', kind=None),
                                            Constant(value='state', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='edi_format', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='state', ctx=Load()),
                                        ],
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
                    name='_process_documents_web_services',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='moves', annotation=None, type_comment=None),
                            arg(arg='formats_to_return', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Generates and returns EDI files for the specified moves.\n        formats_to_return is an optional parameter used to pass a set of codes from\n        the formats we want to return the files for (in case we want to test specific formats).\n        Other formats will still generate documents, they simply won't be returned.\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='moves', ctx=Load()),
                                        attr='edi_document_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_process_documents_web_services',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='with_commit',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='documents_to_return', ctx=Store())],
                            value=Attribute(
                                value=Name(id='moves', ctx=Load()),
                                attr='edi_document_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='formats_to_return', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='documents_to_return', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='documents_to_return', ctx=Load()),
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
                                                        value=Attribute(
                                                            value=Name(id='x', ctx=Load()),
                                                            attr='edi_format_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[Name(id='formats_to_return', ctx=Load())],
                                                ),
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
                            targets=[Name(id='attachments', ctx=Store())],
                            value=Attribute(
                                value=Name(id='documents_to_return', ctx=Load()),
                                attr='attachment_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data_str_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='attachments', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bin_size',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data_str_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='decodebytes',
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
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='data_str_list', ctx=Load()),
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
