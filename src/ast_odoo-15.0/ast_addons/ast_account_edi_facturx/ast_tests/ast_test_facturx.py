Module(
    body=[
        ImportFrom(
            module='freezegun',
            names=[alias(name='freeze_time', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.account_edi.tests.common',
            names=[alias(name='AccountEdiTestCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestAccountEdiFacturx',
            bases=[Name(id='AccountEdiTestCommon', ctx=Load())],
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
                            Constant(value='account_edi_facturx.edi_facturx_1_0_05', kind=None),
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
                                    keyword(
                                        arg='edi_format_ref',
                                        value=Name(id='edi_format_ref', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_10_include',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='type_tax_use', kind=None),
                                            Constant(value='price_include', kind=None),
                                            Constant(value='include_base_amount', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_10_include', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value='sale', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=10, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_20',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='type_tax_use', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_20', kind=None),
                                            Constant(value='percent', kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value='sale', kind=None),
                                            Constant(value=20, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tax_group',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='amount_type', kind=None),
                                            Constant(value='amount', kind=None),
                                            Constant(value='type_tax_use', kind=None),
                                            Constant(value='children_tax_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='tax_group', kind=None),
                                            Constant(value='group', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value='sale', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='tax_10_include',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='tax_20',
                                                                        ctx=Load(),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='invoice',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
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
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='invoice_date', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='journal',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_b',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2017-01-01', kind=None),
                                            Constant(value='2017-01-01', kind=None),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='discount', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='product_a',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
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
                                                                            args=[Constant(value='uom.product_uom_dozen', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=275.0, kind=None),
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value=20.0, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='cls', ctx=Load()),
                                                                                            attr='tax_20',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='expected_invoice_facturx_values',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='\n            <CrossIndustryInvoice>\n                <ExchangedDocumentContext>\n                    <GuidelineSpecifiedDocumentContextParameter>\n                        <ID>urn:cen.eu:en16931:2017</ID>\n                    </GuidelineSpecifiedDocumentContextParameter>\n                </ExchangedDocumentContext>\n                <ExchangedDocument>\n                    <ID>INV/2017/00001</ID>\n                    <TypeCode>380</TypeCode>\n                    <IssueDateTime>\n                        <DateTimeString format="102">20170101</DateTimeString>\n                    </IssueDateTime>\n                </ExchangedDocument>\n                <SupplyChainTradeTransaction>\n                    <IncludedSupplyChainTradeLineItem>\n                        <AssociatedDocumentLineDocument>\n                            <LineID>1</LineID>\n                        </AssociatedDocumentLineDocument>\n                        <SpecifiedTradeProduct>\n                            <Name>product_a</Name>\n                        </SpecifiedTradeProduct>\n                        <SpecifiedLineTradeAgreement>\n                            <GrossPriceProductTradePrice>\n                                <ChargeAmount currencyID="Gol">1100.000</ChargeAmount>\n                                <AppliedTradeAllowanceCharge>\n                                    <ChargeIndicator>\n                                        <Indicator>true</Indicator>\n                                    </ChargeIndicator>\n                                    <CalculationPercent>20.0</CalculationPercent>\n                                </AppliedTradeAllowanceCharge>\n                            </GrossPriceProductTradePrice>\n                        </SpecifiedLineTradeAgreement>\n                        <SpecifiedLineTradeDelivery>\n                            <BilledQuantity>5.0</BilledQuantity>\n                        </SpecifiedLineTradeDelivery>\n                        <SpecifiedLineTradeSettlement>\n                            <ApplicableTradeTax>\n                                <RateApplicablePercent>20.0</RateApplicablePercent>\n                            </ApplicableTradeTax>\n                            <SpecifiedTradeSettlementLineMonetarySummation>\n                                <LineTotalAmount currencyID="Gol">1100.000</LineTotalAmount>\n                            </SpecifiedTradeSettlementLineMonetarySummation>\n                        </SpecifiedLineTradeSettlement>\n                    </IncludedSupplyChainTradeLineItem>\n                    <ApplicableHeaderTradeAgreement>\n                        <SellerTradeParty>\n                            <Name>company_1_data</Name>\n                            <DefinedTradeContact>\n                                <PersonName>company_1_data</PersonName>\n                            </DefinedTradeContact>\n                            <PostalTradeAddress/>\n                        </SellerTradeParty>\n                        <BuyerTradeParty>\n                            <Name>partner_b</Name>\n                            <DefinedTradeContact>\n                                <PersonName>partner_b</PersonName>\n                            </DefinedTradeContact>\n                            <PostalTradeAddress/>\n                        </BuyerTradeParty>\n                        <BuyerOrderReferencedDocument>\n                            <IssuerAssignedID>INV/2017/00001: INV/2017/00001</IssuerAssignedID>\n                        </BuyerOrderReferencedDocument>\n                    </ApplicableHeaderTradeAgreement>\n                    <ApplicableHeaderTradeDelivery/>\n                    <ApplicableHeaderTradeSettlement>\n                        <ApplicableTradeTax>\n                            <CalculatedAmount currencyID="Gol">220.000</CalculatedAmount>\n                            <BasisAmount currencyID="Gol">1100.000</BasisAmount>\n                            <RateApplicablePercent>20.0</RateApplicablePercent>\n                        </ApplicableTradeTax>\n                        <SpecifiedTradePaymentTerms>\n                            <DueDateDateTime>\n                                <DateTimeString>20170101</DateTimeString>\n                            </DueDateDateTime>\n                        </SpecifiedTradePaymentTerms>\n                        <SpecifiedTradeSettlementHeaderMonetarySummation>\n                            <LineTotalAmount currencyID="Gol">1100.000</LineTotalAmount>\n                            <TaxBasisTotalAmount currencyID="Gol">1100.000</TaxBasisTotalAmount>\n                            <TaxTotalAmount currencyID="Gol">220.000</TaxTotalAmount>\n                            <GrandTotalAmount currencyID="Gol">1320.000</GrandTotalAmount>\n                            <TotalPrepaidAmount currencyID="Gol">0.000</TotalPrepaidAmount>\n                            <DuePayableAmount currencyID="Gol">1320.000</DuePayableAmount>\n                        </SpecifiedTradeSettlementHeaderMonetarySummation>\n                    </ApplicableHeaderTradeSettlement>\n                </SupplyChainTradeTransaction>\n            </CrossIndustryInvoice>\n        ', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_facturx',
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
                            value=Constant(value=' Test the generated Facturx Edi attachment without any modification of the invoice. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assert_generated_file_equal',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='expected_invoice_facturx_values',
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
                    name='test_facturx_group_of_taxes',
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
                            value=Constant(value=' Same as above with a group of taxes. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='invoice_line_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='invoice',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='invoice_line_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='tax_ids', kind=None)],
                                                                values=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='tax_group',
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
                        ),
                        Assign(
                            targets=[Name(id='applied_xpath', ctx=Store())],
                            value=Constant(value='\n            <xpath expr="//GrossPriceProductTradePrice/ChargeAmount" position="replace">\n                <ChargeAmount currencyID="Gol">1000.000</ChargeAmount>\n            </xpath>\n            <xpath expr="//SpecifiedLineTradeSettlement" position="replace">\n                <SpecifiedLineTradeSettlement>\n                    <ApplicableTradeTax>\n                        <RateApplicablePercent>10.0</RateApplicablePercent>\n                    </ApplicableTradeTax>\n                    <ApplicableTradeTax>\n                        <RateApplicablePercent>20.0</RateApplicablePercent>\n                    </ApplicableTradeTax>\n                    <SpecifiedTradeSettlementLineMonetarySummation>\n                        <LineTotalAmount currencyID="Gol">1000.000</LineTotalAmount>\n                    </SpecifiedTradeSettlementLineMonetarySummation>\n                </SpecifiedLineTradeSettlement>\n            </xpath>\n            <xpath expr="//ApplicableHeaderTradeSettlement" position="replace">\n                <ApplicableHeaderTradeSettlement>\n                    <ApplicableTradeTax>\n                        <CalculatedAmount currencyID="Gol">100.000</CalculatedAmount>\n                        <BasisAmount currencyID="Gol">1000.000</BasisAmount>\n                        <RateApplicablePercent>10.0</RateApplicablePercent>\n                    </ApplicableTradeTax>\n                    <ApplicableTradeTax>\n                        <CalculatedAmount currencyID="Gol">220.000</CalculatedAmount>\n                        <BasisAmount currencyID="Gol">1100.000</BasisAmount>\n                        <RateApplicablePercent>20.0</RateApplicablePercent>\n                    </ApplicableTradeTax>\n                    <SpecifiedTradePaymentTerms>\n                        <DueDateDateTime>\n                            <DateTimeString>20170101</DateTimeString>\n                        </DueDateDateTime>\n                    </SpecifiedTradePaymentTerms>\n                    <SpecifiedTradeSettlementHeaderMonetarySummation>\n                        <LineTotalAmount currencyID="Gol">1000.000</LineTotalAmount>\n                        <TaxBasisTotalAmount currencyID="Gol">1000.000</TaxBasisTotalAmount>\n                        <TaxTotalAmount currencyID="Gol">320.000</TaxTotalAmount>\n                        <GrandTotalAmount currencyID="Gol">1320.000</GrandTotalAmount>\n                        <TotalPrepaidAmount currencyID="Gol">0.000</TotalPrepaidAmount>\n                        <DuePayableAmount currencyID="Gol">1320.000</DuePayableAmount>\n                    </SpecifiedTradeSettlementHeaderMonetarySummation>\n                </ApplicableHeaderTradeSettlement>\n            </xpath>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assert_generated_file_equal',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='expected_invoice_facturx_values',
                                        ctx=Load(),
                                    ),
                                    Name(id='applied_xpath', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='freeze_time', ctx=Load()),
                            args=[Constant(value='2017-02-01', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_export_pdf',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
                                        ctx=Load(),
                                    ),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pdf_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='edi_format',
                                        ctx=Load(),
                                    ),
                                    attr='_get_embedding_to_invoice_pdf_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='invoice',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='pdf_values', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='factur-x.xml', kind=None),
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
                    name='test_invoice_edi_pdf',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_empty_vendor_bill',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Call(
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
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
                                    attr='update_invoice_from_file',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_facturx', kind=None),
                                    Constant(value='test_file', kind=None),
                                    Constant(value='test_facturx.pdf', kind=None),
                                    Name(id='invoice', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(elts=[], ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='invoice_count', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='amount_total',
                                        ctx=Load(),
                                    ),
                                    Constant(value=525, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_invoice_from_file',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_facturx', kind=None),
                                    Constant(value='test_file', kind=None),
                                    Constant(value='test_facturx.pdf', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='amount_total',
                                        ctx=Load(),
                                    ),
                                    Constant(value=525, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(elts=[], ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Name(id='invoice_count', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
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
                    name='test_invoice_edi_xml',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_empty_vendor_bill',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Call(
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
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
                                    attr='update_invoice_from_file',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_facturx', kind=None),
                                    Constant(value='test_file', kind=None),
                                    Constant(value='test_facturx.xml', kind=None),
                                    Name(id='invoice', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(elts=[], ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='invoice_count', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='amount_total',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4610, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_invoice_from_file',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account_edi_facturx', kind=None),
                                    Constant(value='test_file', kind=None),
                                    Constant(value='test_facturx.xml', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='invoice', ctx=Load()),
                                        attr='amount_total',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4610, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[List(elts=[], ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Name(id='invoice_count', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
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
