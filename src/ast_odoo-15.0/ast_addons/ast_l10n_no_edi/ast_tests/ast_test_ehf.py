Module(
    body=[
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
        ImportFrom(
            module='freezegun',
            names=[alias(name='freeze_time', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestUBL',
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
                            Constant(value='l10n_no.no_chart_template', kind=None),
                            Constant(value='l10n_no_edi.edi_ehf_3', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_data',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='company', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='street', kind=None),
                                            Constant(value='zip', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='l10n_no_bronnoysund_number', kind=None),
                                            Constant(value='vat', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Archefstraat 42', kind=None),
                                            Constant(value='1000', kind=None),
                                            Constant(value='Amsterdam', kind=None),
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
                                                    args=[Constant(value='base.no', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='987654325', kind=None),
                                            Constant(value='NO987654325MVA', kind=None),
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
                                        value=Name(id='cls', ctx=Load()),
                                        attr='partner_a',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='l10n_no_bronnoysund_number', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='vat', kind=None),
                                        ],
                                        values=[
                                            Constant(value='864234232', kind=None),
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
                                                    args=[Constant(value='base.no', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='NO864234232MVA', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='bank_account', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner.bank', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='acc_number', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='86011117947', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_a',
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
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='tax_sale_b',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='amount', kind=None)],
                                        values=[Constant(value=15, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='move_type', kind=None),
                                            Constant(value='partner_bank_id', kind=None),
                                            Constant(value='invoice_date_due', kind=None),
                                            Constant(value='invoice_line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='out_invoice', kind=None),
                                            Attribute(
                                                value=Name(id='bank_account', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2020-12-16', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='price_unit', kind=None),
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
                                                                    Constant(value=150, kind=None),
                                                                    Constant(value=250, kind=None),
                                                                    Constant(value=10, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='cls', ctx=Load()),
                                                                                            attr='tax_sale_a',
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='tax_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='product_b',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value=100, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='cls', ctx=Load()),
                                                                                            attr='tax_sale_b',
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
                                    attr='expected_invoice_values',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='\n            <Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">\n                <cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>\n                <cbc:ProfileID>urn:fdc:peppol.eu:2017:poacc:billing:01:1.0</cbc:ProfileID>\n                <cbc:ID>INV/2020/00001</cbc:ID>\n                <cbc:IssueDate>2020-12-16</cbc:IssueDate>\n                <cbc:DueDate>2020-12-16</cbc:DueDate>\n                <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>\n                <cbc:DocumentCurrencyCode>NOK</cbc:DocumentCurrencyCode>\n                <cbc:BuyerReference>partner_a</cbc:BuyerReference>\n                <cac:AccountingSupplierParty>\n            <cac:Party>\n                <cbc:EndpointID schemeID="0192">987654325</cbc:EndpointID>\n                <cac:PartyName>\n                    <cbc:Name>company_1_data</cbc:Name>\n                </cac:PartyName>\n                <cac:PostalAddress>\n                    <cbc:StreetName>Archefstraat 42</cbc:StreetName>\n                    <cbc:CityName>Amsterdam</cbc:CityName>\n                    <cbc:PostalZone>1000</cbc:PostalZone>\n                    <cac:Country>\n                        <cbc:IdentificationCode>NO</cbc:IdentificationCode>\n                    </cac:Country>\n                </cac:PostalAddress>\n                <cac:PartyTaxScheme>\n                    <cbc:CompanyID>NO987654325MVA</cbc:CompanyID>\n                    <cac:TaxScheme>\n                        <cbc:ID>VAT</cbc:ID>\n                    </cac:TaxScheme>\n                </cac:PartyTaxScheme>\n                <cac:PartyTaxScheme>\n                    <cbc:CompanyID>Foretaksregisteret</cbc:CompanyID>\n                    <cac:TaxScheme>\n                        <cbc:ID>TAX</cbc:ID>\n                    </cac:TaxScheme>\n                </cac:PartyTaxScheme>\n                <cac:PartyLegalEntity>\n                    <cbc:RegistrationName>company_1_data</cbc:RegistrationName>\n                </cac:PartyLegalEntity>\n                <cac:Contact>\n                    <cbc:Name>company_1_data</cbc:Name>\n                  </cac:Contact>\n            </cac:Party>\n        </cac:AccountingSupplierParty>\n            <cac:AccountingCustomerParty>\n            <cac:Party>\n                <cbc:EndpointID schemeID="0192">864234232</cbc:EndpointID>\n                <cac:PartyName>\n                    <cbc:Name>partner_a</cbc:Name>\n                </cac:PartyName>\n                <cac:PostalAddress>\n                    <cac:Country>\n                        <cbc:IdentificationCode>NO</cbc:IdentificationCode>\n                    </cac:Country>\n                </cac:PostalAddress>\n                <cac:PartyTaxScheme>\n                    <cbc:CompanyID>NO864234232MVA</cbc:CompanyID>\n                    <cac:TaxScheme>\n                        <cbc:ID>VAT</cbc:ID>\n                    </cac:TaxScheme>\n                </cac:PartyTaxScheme>\n                <cac:PartyLegalEntity>\n                    <cbc:RegistrationName>partner_a</cbc:RegistrationName>\n                </cac:PartyLegalEntity>\n                <cac:Contact>\n                    <cbc:Name>partner_a</cbc:Name>\n                  </cac:Contact>\n            </cac:Party>\n        </cac:AccountingCustomerParty>\n                <cac:PaymentMeans>\n                    <cbc:PaymentMeansCode>31</cbc:PaymentMeansCode>\n                    <cac:PayeeFinancialAccount>\n                        <cbc:ID>86011117947</cbc:ID>\n                    </cac:PayeeFinancialAccount>\n                </cac:PaymentMeans>\n                <cac:TaxTotal>\n                    <cbc:TaxAmount currencyID="NOK">8617.50</cbc:TaxAmount>\n                    <cac:TaxSubtotal>\n                        <cbc:TaxableAmount currencyID="NOK">33750.00</cbc:TaxableAmount>\n                        <cbc:TaxAmount currencyID="NOK">8437.50</cbc:TaxAmount>\n                        <cac:TaxCategory>\n                            <cbc:ID>S</cbc:ID>\n                            <cbc:Percent>25.0</cbc:Percent>\n                            <cac:TaxScheme>\n                                <cbc:ID>VAT</cbc:ID>\n                            </cac:TaxScheme>\n                        </cac:TaxCategory>\n                    </cac:TaxSubtotal><cac:TaxSubtotal>\n                        <cbc:TaxableAmount currencyID="NOK">1200.00</cbc:TaxableAmount>\n                        <cbc:TaxAmount currencyID="NOK">180.00</cbc:TaxAmount>\n                        <cac:TaxCategory>\n                            <cbc:ID>S</cbc:ID>\n                            <cbc:Percent>15.0</cbc:Percent>\n                            <cac:TaxScheme>\n                                <cbc:ID>VAT</cbc:ID>\n                            </cac:TaxScheme>\n                        </cac:TaxCategory>\n                    </cac:TaxSubtotal>\n                </cac:TaxTotal>\n                <cac:LegalMonetaryTotal>\n                    <cbc:LineExtensionAmount currencyID="NOK">34950.00</cbc:LineExtensionAmount>\n                    <cbc:TaxExclusiveAmount currencyID="NOK">34950.00</cbc:TaxExclusiveAmount>\n                    <cbc:TaxInclusiveAmount currencyID="NOK">43567.50</cbc:TaxInclusiveAmount>\n                    <cbc:PrepaidAmount currencyID="NOK">0.00</cbc:PrepaidAmount>\n                    <cbc:PayableAmount currencyID="NOK">43567.50</cbc:PayableAmount>\n                </cac:LegalMonetaryTotal>\n            <cac:InvoiceLine>\n                <cbc:ID>1</cbc:ID>\n                <cbc:Note>Discount (10.0 %)</cbc:Note>\n                <cbc:InvoicedQuantity unitCode="ZZ">150.0</cbc:InvoicedQuantity>\n                <cbc:LineExtensionAmount currencyID="NOK">33750.00</cbc:LineExtensionAmount>\n                <cac:Item>\n                    <cbc:Description>product_a</cbc:Description>\n                    <cbc:Name>product_a</cbc:Name>\n                    <cac:ClassifiedTaxCategory>\n                        <cbc:ID>S</cbc:ID>\n                        <cbc:Percent>25.0</cbc:Percent>\n                        <cac:TaxScheme>\n                            <cbc:ID>VAT</cbc:ID>\n                        </cac:TaxScheme>\n                    </cac:ClassifiedTaxCategory>\n                </cac:Item>\n                <cac:Price>\n                    <cbc:PriceAmount currencyID="NOK">225.00</cbc:PriceAmount>\n                    <cbc:BaseQuantity>150.0</cbc:BaseQuantity>\n                </cac:Price>\n            </cac:InvoiceLine>\n            <cac:InvoiceLine>\n                <cbc:ID>2</cbc:ID>\n                <cbc:InvoicedQuantity unitCode="ZZ">12.0</cbc:InvoicedQuantity>\n                <cbc:LineExtensionAmount currencyID="NOK">1200.00</cbc:LineExtensionAmount>\n                <cac:Item>\n                    <cbc:Description>product_b</cbc:Description>\n                    <cbc:Name>product_b</cbc:Name>\n                    <cac:ClassifiedTaxCategory>\n                        <cbc:ID>S</cbc:ID>\n                        <cbc:Percent>15.0</cbc:Percent>\n                        <cac:TaxScheme>\n                            <cbc:ID>VAT</cbc:ID>\n                        </cac:TaxScheme>\n                    </cac:ClassifiedTaxCategory>\n                </cac:Item>\n                <cac:Price>\n                    <cbc:PriceAmount currencyID="NOK">100.00</cbc:PriceAmount>\n                    <cbc:BaseQuantity>12.0</cbc:BaseQuantity>\n                </cac:Price>\n            </cac:InvoiceLine>\n            </Invoice>\n        ', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_ehf_import',
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice_count', ctx=Store())],
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
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
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
                                    Constant(value='l10n_no_edi', kind=None),
                                    Constant(value='test_xml_file', kind=None),
                                    Constant(value='ehf_test.xml', kind=None),
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
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
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
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='invoice', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='amount_total', kind=None),
                                                    Constant(value='amount_tax', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='partner_a',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1801.78, kind=None),
                                                    Constant(value=365.28, kind=None),
                                                ],
                                            ),
                                        ],
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
                    name='test_ehf_export',
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
                                        attr='expected_invoice_values',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='freeze_time', ctx=Load()),
                            args=[Constant(value='2020-12-16', kind=None)],
                            keywords=[],
                        ),
                    ],
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
