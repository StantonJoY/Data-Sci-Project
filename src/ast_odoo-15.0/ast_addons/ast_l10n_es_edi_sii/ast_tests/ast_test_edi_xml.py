Module(
    body=[
        ImportFrom(
            module='common',
            names=[alias(name='TestEsEdiCommon', asname=None)],
            level=1,
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='freezegun',
            names=[alias(name='freeze_time', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='mocked_l10n_es_edi_call_web_service_sign',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='edi_format', annotation=None, type_comment=None),
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='TestEdiXmls',
            bases=[Name(id='TestEsEdiCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                    attr='setUpClass',
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
                                        value=Name(id='cls', ctx=Load()),
                                        attr='certificate',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date_start', kind=None),
                                            Constant(value='date_end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2019-01-01 01:00:00', kind=None),
                                            Constant(value='2021-01-01 01:00:00', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_010_out_invoice_s_iva10b_s_iva21s',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva10b', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva21s', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='INV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseTipoOperacion', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='PrestacionServicios', kind=None),
                                                                            Constant(value='Entrega', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='NoExenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='TipoNoExenta', kind=None),
                                                                                                    Constant(value='DesgloseIVA', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Constant(value='S1', kind=None),
                                                                                                    Dict(
                                                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                                                        values=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                                                            Constant(value='CuotaRepercutida', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Constant(value=21.0, kind=None),
                                                                                                                            Constant(value=200.0, kind=None),
                                                                                                                            Constant(value=42.0, kind=None),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='NoExenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='TipoNoExenta', kind=None),
                                                                                                    Constant(value='DesgloseIVA', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Constant(value='S1', kind=None),
                                                                                                    Dict(
                                                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                                                        values=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                                                            Constant(value='CuotaRepercutida', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Constant(value=10.0, kind=None),
                                                                                                                            Constant(value=100.0, kind=None),
                                                                                                                            Constant(value=10.0, kind=None),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
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
                                                                ],
                                                            ),
                                                            Constant(value=352.0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='IDOtro', kind=None),
                                                                    Constant(value='NombreRazon', kind=None),
                                                                ],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='ID', kind=None),
                                                                            Constant(value='IDType', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='BE0477472701', kind=None),
                                                                            Constant(value='02', kind=None),
                                                                        ],
                                                                    ),
                                                                    Constant(value='partner_a', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_020_out_invoice_s_iva10b_s_iva0_ns',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva10b', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_ns', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='INV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseFactura', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='Sujeta', kind=None)],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='NoExenta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='TipoNoExenta', kind=None),
                                                                                            Constant(value='DesgloseIVA', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='S1', kind=None),
                                                                                            Dict(
                                                                                                keys=[Constant(value='DetalleIVA', kind=None)],
                                                                                                values=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='TipoImpositivo', kind=None),
                                                                                                                    Constant(value='BaseImponible', kind=None),
                                                                                                                    Constant(value='CuotaRepercutida', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value=10.0, kind=None),
                                                                                                                    Constant(value=100.0, kind=None),
                                                                                                                    Constant(value=10.0, kind=None),
                                                                                                                ],
                                                                                                            ),
                                                                                                        ],
                                                                                                        ctx=Load(),
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
                                                            Constant(value=110.0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_030_out_invoice_s_iva10b_s_req014_s_iva21s_s_req52',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='s_iva10b', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='s_req014', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='s_iva21s', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='s_req52', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='INV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseTipoOperacion', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='PrestacionServicios', kind=None),
                                                                            Constant(value='Entrega', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='NoExenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='TipoNoExenta', kind=None),
                                                                                                    Constant(value='DesgloseIVA', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Constant(value='S1', kind=None),
                                                                                                    Dict(
                                                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                                                        values=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                                                            Constant(value='CuotaRepercutida', kind=None),
                                                                                                                            Constant(value='CuotaRecargoEquivalencia', kind=None),
                                                                                                                            Constant(value='TipoRecargoEquivalencia', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Constant(value=21.0, kind=None),
                                                                                                                            Constant(value=200.0, kind=None),
                                                                                                                            Constant(value=42.0, kind=None),
                                                                                                                            Constant(value=10.4, kind=None),
                                                                                                                            Constant(value=5.2, kind=None),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='NoExenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='TipoNoExenta', kind=None),
                                                                                                    Constant(value='DesgloseIVA', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Constant(value='S1', kind=None),
                                                                                                    Dict(
                                                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                                                        values=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                                                            Constant(value='CuotaRepercutida', kind=None),
                                                                                                                            Constant(value='CuotaRecargoEquivalencia', kind=None),
                                                                                                                            Constant(value='TipoRecargoEquivalencia', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Constant(value=10.0, kind=None),
                                                                                                                            Constant(value=100.0, kind=None),
                                                                                                                            Constant(value=10.0, kind=None),
                                                                                                                            Constant(value=1.4, kind=None),
                                                                                                                            Constant(value=1.4, kind=None),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
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
                                                                ],
                                                            ),
                                                            Constant(value=363.8, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='IDOtro', kind=None),
                                                                    Constant(value='NombreRazon', kind=None),
                                                                ],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='ID', kind=None),
                                                                            Constant(value='IDType', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='BE0477472701', kind=None),
                                                                            Constant(value='02', kind=None),
                                                                        ],
                                                                    ),
                                                                    Constant(value='partner_a', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_040_out_refund_s_iva10b_s_iva10b_s_iva21s',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='out_refund', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva10b', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva10b', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva21s', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='RINV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='TipoRectificativa', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='R1', kind=None),
                                                            Constant(value='I', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseTipoOperacion', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='PrestacionServicios', kind=None),
                                                                            Constant(value='Entrega', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='NoExenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='TipoNoExenta', kind=None),
                                                                                                    Constant(value='DesgloseIVA', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Constant(value='S1', kind=None),
                                                                                                    Dict(
                                                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                                                        values=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                                                            Constant(value='CuotaRepercutida', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Constant(value=21.0, kind=None),
                                                                                                                            UnaryOp(
                                                                                                                                op=USub(),
                                                                                                                                operand=Constant(value=200.0, kind=None),
                                                                                                                            ),
                                                                                                                            UnaryOp(
                                                                                                                                op=USub(),
                                                                                                                                operand=Constant(value=42.0, kind=None),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='NoExenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='TipoNoExenta', kind=None),
                                                                                                    Constant(value='DesgloseIVA', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Constant(value='S1', kind=None),
                                                                                                    Dict(
                                                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                                                        values=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                                                            Constant(value='CuotaRepercutida', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Constant(value=10.0, kind=None),
                                                                                                                            UnaryOp(
                                                                                                                                op=USub(),
                                                                                                                                operand=Constant(value=200.0, kind=None),
                                                                                                                            ),
                                                                                                                            UnaryOp(
                                                                                                                                op=USub(),
                                                                                                                                operand=Constant(value=20.0, kind=None),
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
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
                                                                ],
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=462.0, kind=None),
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='IDOtro', kind=None),
                                                                    Constant(value='NombreRazon', kind=None),
                                                                ],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='ID', kind=None),
                                                                            Constant(value='IDType', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='BE0477472701', kind=None),
                                                                            Constant(value='02', kind=None),
                                                                        ],
                                                                    ),
                                                                    Constant(value='partner_a', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_050_out_invoice_s_iva0_sp_i_s_iva0_ic',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_sp_i', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_ic', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='INV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseTipoOperacion', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='PrestacionServicios', kind=None),
                                                                            Constant(value='Entrega', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='NoSujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='ImportePorArticulos7_14_Otros', kind=None)],
                                                                                        values=[Constant(value=100.0, kind=None)],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='Exenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='DetalleExenta', kind=None)],
                                                                                                values=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='BaseImponible', kind=None),
                                                                                                                    Constant(value='CausaExencion', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value=200.0, kind=None),
                                                                                                                    Constant(value='E5', kind=None),
                                                                                                                ],
                                                                                                            ),
                                                                                                        ],
                                                                                                        ctx=Load(),
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
                                                            Constant(value=300.0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='IDOtro', kind=None),
                                                                    Constant(value='NombreRazon', kind=None),
                                                                ],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='ID', kind=None),
                                                                            Constant(value='IDType', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='BE0477472701', kind=None),
                                                                            Constant(value='02', kind=None),
                                                                        ],
                                                                    ),
                                                                    Constant(value='partner_a', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_060_out_refund_s_iva0_sp_i_s_iva0_ic',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='out_refund', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_sp_i', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_ic', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='RINV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='TipoRectificativa', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='R1', kind=None),
                                                            Constant(value='I', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseTipoOperacion', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='PrestacionServicios', kind=None),
                                                                            Constant(value='Entrega', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='NoSujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='ImportePorArticulos7_14_Otros', kind=None)],
                                                                                        values=[
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=100.0, kind=None),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='Exenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='DetalleExenta', kind=None)],
                                                                                                values=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='BaseImponible', kind=None),
                                                                                                                    Constant(value='CausaExencion', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    UnaryOp(
                                                                                                                        op=USub(),
                                                                                                                        operand=Constant(value=200.0, kind=None),
                                                                                                                    ),
                                                                                                                    Constant(value='E5', kind=None),
                                                                                                                ],
                                                                                                            ),
                                                                                                        ],
                                                                                                        ctx=Load(),
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
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=300.0, kind=None),
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='IDOtro', kind=None),
                                                                    Constant(value='NombreRazon', kind=None),
                                                                ],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='ID', kind=None),
                                                                            Constant(value='IDType', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='BE0477472701', kind=None),
                                                                            Constant(value='02', kind=None),
                                                                        ],
                                                                    ),
                                                                    Constant(value='partner_a', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_070_out_invoice_s_iva_e_s_iva0_e',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva_e', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_e', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='INV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseTipoOperacion', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='PrestacionServicios', kind=None),
                                                                            Constant(value='Entrega', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='NoSujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='ImportePorArticulos7_14_Otros', kind=None)],
                                                                                        values=[Constant(value=100.0, kind=None)],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='Exenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='DetalleExenta', kind=None)],
                                                                                                values=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='BaseImponible', kind=None),
                                                                                                                    Constant(value='CausaExencion', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value=200.0, kind=None),
                                                                                                                    Constant(value='E2', kind=None),
                                                                                                                ],
                                                                                                            ),
                                                                                                        ],
                                                                                                        ctx=Load(),
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
                                                            Constant(value=300.0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='IDOtro', kind=None),
                                                                    Constant(value='NombreRazon', kind=None),
                                                                ],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='ID', kind=None),
                                                                            Constant(value='IDType', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='BE0477472701', kind=None),
                                                                            Constant(value='02', kind=None),
                                                                        ],
                                                                    ),
                                                                    Constant(value='partner_a', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_080_out_refund_s_iva0_sp_i_s_iva0_ic',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='out_refund', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_sp_i', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_ic', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='RINV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='TipoRectificativa', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='R1', kind=None),
                                                            Constant(value='I', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseTipoOperacion', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='PrestacionServicios', kind=None),
                                                                            Constant(value='Entrega', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='NoSujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='ImportePorArticulos7_14_Otros', kind=None)],
                                                                                        values=[
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=100.0, kind=None),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='Exenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='DetalleExenta', kind=None)],
                                                                                                values=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='BaseImponible', kind=None),
                                                                                                                    Constant(value='CausaExencion', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    UnaryOp(
                                                                                                                        op=USub(),
                                                                                                                        operand=Constant(value=200.0, kind=None),
                                                                                                                    ),
                                                                                                                    Constant(value='E5', kind=None),
                                                                                                                ],
                                                                                                            ),
                                                                                                        ],
                                                                                                        ctx=Load(),
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
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=300.0, kind=None),
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='IDOtro', kind=None),
                                                                    Constant(value='NombreRazon', kind=None),
                                                                ],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='ID', kind=None),
                                                                            Constant(value='IDType', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='BE0477472701', kind=None),
                                                                            Constant(value='02', kind=None),
                                                                        ],
                                                                    ),
                                                                    Constant(value='partner_a', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_085_out_refund_s_iva0_sp_i_s_iva0_ic_multi_currency',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='out_refund', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_a',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='currency_id',
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='currency_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_sp_i', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=400.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='s_iva0_ic', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='RINV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='TipoRectificativa', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='R1', kind=None),
                                                            Constant(value='I', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseTipoOperacion', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='PrestacionServicios', kind=None),
                                                                            Constant(value='Entrega', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='NoSujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='ImportePorArticulos7_14_Otros', kind=None)],
                                                                                        values=[
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=100.0, kind=None),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Dict(
                                                                                keys=[Constant(value='Sujeta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='Exenta', kind=None)],
                                                                                        values=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='DetalleExenta', kind=None)],
                                                                                                values=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='BaseImponible', kind=None),
                                                                                                                    Constant(value='CausaExencion', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    UnaryOp(
                                                                                                                        op=USub(),
                                                                                                                        operand=Constant(value=200.0, kind=None),
                                                                                                                    ),
                                                                                                                    Constant(value='E5', kind=None),
                                                                                                                ],
                                                                                                            ),
                                                                                                        ],
                                                                                                        ctx=Load(),
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
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=300.0, kind=None),
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='IDOtro', kind=None),
                                                                    Constant(value='NombreRazon', kind=None),
                                                                ],
                                                                values=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='ID', kind=None),
                                                                            Constant(value='IDType', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='BE0477472701', kind=None),
                                                                            Constant(value='02', kind=None),
                                                                        ],
                                                                    ),
                                                                    Constant(value='partner_a', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_090_in_invoice_p_iva10_bc_p_irpf19_p_iva21_sc_p_irpf19',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='in_invoice', kind=None),
                                            ),
                                            keyword(
                                                arg='ref',
                                                value=Constant(value='sup0001', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='l10n_es_registration_date',
                                                value=Constant(value='2019-01-02', kind=None),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_iva10_bc', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_irpf19', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_iva21_sc', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_irpf19', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='FacturaRecibida', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01-01-2019', kind=None),
                                                            Constant(value='sup0001', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='F35999705', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='FechaRegContable', kind=None),
                                                            Constant(value='DesgloseFactura', kind=None),
                                                            Constant(value='CuotaDeducible', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='manual', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value=352.0, kind=None),
                                                            Constant(value='02-01-2019', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseIVA', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=100.0, kind=None),
                                                                                            Constant(value=10.0, kind=None),
                                                                                            Constant(value=10.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=200.0, kind=None),
                                                                                            Constant(value=42.0, kind=None),
                                                                                            Constant(value=21.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=52.0, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Periodo', kind=None),
                                                            Constant(value='Ejercicio', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01', kind=None),
                                                            Constant(value='2019', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_100_in_refund_p_iva10_bc',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='in_refund', kind=None),
                                            ),
                                            keyword(
                                                arg='ref',
                                                value=Constant(value='sup0001', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='l10n_es_registration_date',
                                                value=Constant(value='2019-01-02', kind=None),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='p_iva10_bc', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='FacturaRecibida', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01-01-2019', kind=None),
                                                            Constant(value='sup0001', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='F35999705', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='TipoRectificativa', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='FechaRegContable', kind=None),
                                                            Constant(value='DesgloseFactura', kind=None),
                                                            Constant(value='CuotaDeducible', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='R4', kind=None),
                                                            Constant(value='I', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='manual', kind=None),
                                                            Constant(value='01', kind=None),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=110.0, kind=None),
                                                            ),
                                                            Constant(value='02-01-2019', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseIVA', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=100.0, kind=None),
                                                                                            ),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=10.0, kind=None),
                                                                                            ),
                                                                                            Constant(value=10.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=10.0, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Periodo', kind=None),
                                                            Constant(value='Ejercicio', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01', kind=None),
                                                            Constant(value='2019', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_110_in_invoice_p_iva10_bc_p_req014_p_iva21_sc_p_req52',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='in_invoice', kind=None),
                                            ),
                                            keyword(
                                                arg='ref',
                                                value=Constant(value='sup0001', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='l10n_es_registration_date',
                                                value=Constant(value='2019-01-02', kind=None),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_iva10_bc', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_req014', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_iva21_sc', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_req52', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='FacturaRecibida', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01-01-2019', kind=None),
                                                            Constant(value='sup0001', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='F35999705', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='FechaRegContable', kind=None),
                                                            Constant(value='DesgloseFactura', kind=None),
                                                            Constant(value='CuotaDeducible', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='manual', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value=363.8, kind=None),
                                                            Constant(value='02-01-2019', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseIVA', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                            Constant(value='CuotaRecargoEquivalencia', kind=None),
                                                                                            Constant(value='TipoRecargoEquivalencia', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=100.0, kind=None),
                                                                                            Constant(value=10.0, kind=None),
                                                                                            Constant(value=10.0, kind=None),
                                                                                            Constant(value=1.4, kind=None),
                                                                                            Constant(value=1.4, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                            Constant(value='CuotaRecargoEquivalencia', kind=None),
                                                                                            Constant(value='TipoRecargoEquivalencia', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=200.0, kind=None),
                                                                                            Constant(value=42.0, kind=None),
                                                                                            Constant(value=21.0, kind=None),
                                                                                            Constant(value=10.4, kind=None),
                                                                                            Constant(value=5.2, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=52.0, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Periodo', kind=None),
                                                            Constant(value='Ejercicio', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01', kind=None),
                                                            Constant(value='2019', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_120_in_invoice_p_iva21_sp_ex',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='in_invoice', kind=None),
                                            ),
                                            keyword(
                                                arg='ref',
                                                value=Constant(value='sup0001', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='l10n_es_registration_date',
                                                value=Constant(value='2019-01-02', kind=None),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='p_iva21_sp_ex', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='FacturaRecibida', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01-01-2019', kind=None),
                                                            Constant(value='sup0001', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='F35999705', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='FechaRegContable', kind=None),
                                                            Constant(value='DesgloseFactura', kind=None),
                                                            Constant(value='CuotaDeducible', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='manual', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value=121.0, kind=None),
                                                            Constant(value='02-01-2019', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='InversionSujetoPasivo', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=100.0, kind=None),
                                                                                            Constant(value=21.0, kind=None),
                                                                                            Constant(value=21.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=21.0, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Periodo', kind=None),
                                                            Constant(value='Ejercicio', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01', kind=None),
                                                            Constant(value='2019', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_130_in_invoice_p_iva0_ns_p_iva10_bc',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='in_invoice', kind=None),
                                            ),
                                            keyword(
                                                arg='ref',
                                                value=Constant(value='sup0001', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='l10n_es_registration_date',
                                                value=Constant(value='2019-01-02', kind=None),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='p_iva0_ns', kind=None)],
                                                                                        keywords=[],
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
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_get_tax_by_xml_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='p_iva10_bc', kind=None)],
                                                                                        keywords=[],
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='FacturaRecibida', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01-01-2019', kind=None),
                                                            Constant(value='sup0001', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='F35999705', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='FechaRegContable', kind=None),
                                                            Constant(value='DesgloseFactura', kind=None),
                                                            Constant(value='CuotaDeducible', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='manual', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value=320.0, kind=None),
                                                            Constant(value='02-01-2019', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseIVA', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[Constant(value='BaseImponible', kind=None)],
                                                                                        values=[Constant(value=100.0, kind=None)],
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=200.0, kind=None),
                                                                                            Constant(value=10.0, kind=None),
                                                                                            Constant(value=20.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=20.0, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Periodo', kind=None),
                                                            Constant(value='Ejercicio', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01', kind=None),
                                                            Constant(value='2019', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_140_out_invoice_s_iva10b_s_irpf1',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='s_iva10b', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='s_irpf1', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                    Constant(value='FacturaExpedida', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                        ],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='59962470K', kind=None)],
                                                            ),
                                                            Constant(value='INV/2019/00001', kind=None),
                                                            Constant(value='01-01-2019', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Ejercicio', kind=None),
                                                            Constant(value='Periodo', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2019', kind=None),
                                                            Constant(value='01', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='TipoDesglose', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseFactura', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='Sujeta', kind=None)],
                                                                        values=[
                                                                            Dict(
                                                                                keys=[Constant(value='NoExenta', kind=None)],
                                                                                values=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='TipoNoExenta', kind=None),
                                                                                            Constant(value='DesgloseIVA', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value='S1', kind=None),
                                                                                            Dict(
                                                                                                keys=[Constant(value='DetalleIVA', kind=None)],
                                                                                                values=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='TipoImpositivo', kind=None),
                                                                                                                    Constant(value='BaseImponible', kind=None),
                                                                                                                    Constant(value='CuotaRepercutida', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Constant(value=10.0, kind=None),
                                                                                                                    Constant(value=100.0, kind=None),
                                                                                                                    Constant(value=10.0, kind=None),
                                                                                                                ],
                                                                                                            ),
                                                                                                        ],
                                                                                                        ctx=Load(),
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
                                                            Constant(value=110.0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_150_in_invoice_p_iva10_bc_p_irpf1',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='in_invoice', kind=None),
                                            ),
                                            keyword(
                                                arg='ref',
                                                value=Constant(value='sup0001', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='l10n_es_registration_date',
                                                value=Constant(value='2019-01-02', kind=None),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_iva10_bc', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_irpf1', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='FacturaRecibida', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01-01-2019', kind=None),
                                                            Constant(value='sup0001', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='F35999705', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='FechaRegContable', kind=None),
                                                            Constant(value='DesgloseFactura', kind=None),
                                                            Constant(value='CuotaDeducible', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='F1', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='manual', kind=None),
                                                            Constant(value='01', kind=None),
                                                            Constant(value=110.0, kind=None),
                                                            Constant(value='02-01-2019', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseIVA', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Constant(value=100.0, kind=None),
                                                                                            Constant(value=10.0, kind=None),
                                                                                            Constant(value=10.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=10.0, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Periodo', kind=None),
                                                            Constant(value='Ejercicio', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01', kind=None),
                                                            Constant(value='2019', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_160_in_refund_p_iva10_bc_p_irpf1',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='in_refund', kind=None),
                                            ),
                                            keyword(
                                                arg='ref',
                                                value=Constant(value='sup0001', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='l10n_es_registration_date',
                                                value=Constant(value='2019-01-02', kind=None),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=100.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_iva10_bc', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_irpf1', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='FacturaRecibida', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01-01-2019', kind=None),
                                                            Constant(value='sup0001', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='F35999705', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='TipoRectificativa', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='FechaRegContable', kind=None),
                                                            Constant(value='DesgloseFactura', kind=None),
                                                            Constant(value='CuotaDeducible', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='R4', kind=None),
                                                            Constant(value='I', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='manual', kind=None),
                                                            Constant(value='01', kind=None),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=110.0, kind=None),
                                                            ),
                                                            Constant(value='02-01-2019', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseIVA', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=100.0, kind=None),
                                                                                            ),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=10.0, kind=None),
                                                                                            ),
                                                                                            Constant(value=10.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=10.0, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Periodo', kind=None),
                                                            Constant(value='Ejercicio', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01', kind=None),
                                                            Constant(value='2019', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_165_in_refund_p_iva10_bc_p_irpf1_multi_currency',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='freeze_time', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frozen_today',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[Constant(value='odoo.addons.l10n_es_edi_sii.models.account_edi_format.AccountEdiFormat._l10n_es_edi_call_web_service_sign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='new',
                                                value=Name(id='mocked_l10n_es_edi_call_web_service_sign', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='invoice', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_invoice',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_type',
                                                value=Constant(value='in_refund', kind=None),
                                            ),
                                            keyword(
                                                arg='ref',
                                                value=Constant(value='sup0001', kind=None),
                                            ),
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='partner_b',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='currency_id',
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='currency_data',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='currency', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='l10n_es_registration_date',
                                                value=Constant(value='2019-01-02', kind=None),
                                            ),
                                            keyword(
                                                arg='invoice_line_ids',
                                                value=List(
                                                    elts=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='price_unit', kind=None),
                                                                Constant(value='tax_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=200.0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_iva10_bc', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='_get_tax_by_xml_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='p_irpf1', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
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
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
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
                                Assign(
                                    targets=[Name(id='generated_files', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_process_documents_web_services',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='invoice', ctx=Load()),
                                            Set(
                                                elts=[Constant(value='es_sii', kind=None)],
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='generated_files', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='json_file', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='generated_files', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='json_file', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='IDFactura', kind=None),
                                                    Constant(value='FacturaRecibida', kind=None),
                                                    Constant(value='PeriodoLiquidacion', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='FechaExpedicionFacturaEmisor', kind=None),
                                                            Constant(value='NumSerieFacturaEmisor', kind=None),
                                                            Constant(value='IDEmisorFactura', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01-01-2019', kind=None),
                                                            Constant(value='sup0001', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='NIF', kind=None)],
                                                                values=[Constant(value='F35999705', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='TipoFactura', kind=None),
                                                            Constant(value='TipoRectificativa', kind=None),
                                                            Constant(value='Contraparte', kind=None),
                                                            Constant(value='DescripcionOperacion', kind=None),
                                                            Constant(value='ClaveRegimenEspecialOTrascendencia', kind=None),
                                                            Constant(value='ImporteTotal', kind=None),
                                                            Constant(value='FechaRegContable', kind=None),
                                                            Constant(value='DesgloseFactura', kind=None),
                                                            Constant(value='CuotaDeducible', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='R4', kind=None),
                                                            Constant(value='I', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='NombreRazon', kind=None),
                                                                    Constant(value='NIF', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='partner_b', kind=None),
                                                                    Constant(value='F35999705', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='manual', kind=None),
                                                            Constant(value='01', kind=None),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=110.0, kind=None),
                                                            ),
                                                            Constant(value='02-01-2019', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='DesgloseIVA', kind=None)],
                                                                values=[
                                                                    Dict(
                                                                        keys=[Constant(value='DetalleIVA', kind=None)],
                                                                        values=[
                                                                            List(
                                                                                elts=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='BaseImponible', kind=None),
                                                                                            Constant(value='CuotaSoportada', kind=None),
                                                                                            Constant(value='TipoImpositivo', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=100.0, kind=None),
                                                                                            ),
                                                                                            UnaryOp(
                                                                                                op=USub(),
                                                                                                operand=Constant(value=10.0, kind=None),
                                                                                            ),
                                                                                            Constant(value=10.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=10.0, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='Periodo', kind=None),
                                                            Constant(value='Ejercicio', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='01', kind=None),
                                                            Constant(value='2019', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install_l10n', kind=None),
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
